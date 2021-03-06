from django.db import models
import importlib
from ..lib.obj import BasicBotInterface
from ..utils import get_bot_interfaces


LOGIC_INTERFACE_CHOICES = [
	(interface, interface) for interface in get_bot_interfaces()
]


class Bot(models.Model):

	token = models.CharField(max_length=1000)
	logic_interface = models.CharField(max_length=1024, choices=LOGIC_INTERFACE_CHOICES)

	def __str__(self):
		return self.logic_interface

	def get_interface(self) -> BasicBotInterface:
		interface_name = self.logic_interface.split(".")[-1]
		module_path = self.logic_interface.replace(f".{interface_name}", "")
		module = importlib.import_module(module_path)
		interface = getattr(module, interface_name)
		return interface(self.token)

	def get_or_create_user(self, chat_id):
		result = self.botuser_set.model.objects.get_or_create(
			chat_id=str(chat_id),
			defaults={
				"bot": self
			}
		)
		return result

	def start_polling(self):
		i = self.get_interface()
		i.bot.polling(none_stop=True)