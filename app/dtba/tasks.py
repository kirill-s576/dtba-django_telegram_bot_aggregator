from celery import shared_task
from .models import Bot


@shared_task
def handle_bot_message(bot_id, call_or_message):
    bot = Bot.objects.get(id=bot_id)
    interface = bot.get_interface()

