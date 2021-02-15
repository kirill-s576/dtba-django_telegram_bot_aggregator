from dtba.lib.obj import BasicBotInterface
from dtba.lib.obj.conditions import BaseCondition
from dtba.lib.obj.handlers import BaseHandler
from dtba.lib.obj.handlers import handler_action

from dtba.lib.obj.conditions import IsText, IsFile, IsCallback

from dtba.lib.obj.message import TextResponseMessage


class ContainsText(BaseCondition):

    text:str = ""

    def is_valid(self):
        if self.text in self.request.message.text:
            return True
        return False


class TestHandler(BaseHandler):

    @handler_action(
        conditions_list=[
            IsText,
            ContainsText(text="start"),
        ]
    )
    def show_menu(self, request):
        print(request.message.chat.id)
        print(request.url)
        print(request.message.text)
        print(request.user_model)
        print(request.bot_model)
        print(request.is_new_user)
        message = TextResponseMessage(request, "Hello World!")
        result = message.send()
        print(result)

class TestBot(BasicBotInterface):

    handlers = [
        TestHandler
    ]

if __name__ == '__main__':
    i = TestBot("1572621465:AAEWZzXzWn0MJ8Lqb8YIf-sggZzMEtkvQEQ")
    i.bot.polling(none_stop=True)