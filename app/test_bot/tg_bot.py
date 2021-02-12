from dtba.lib.obj import BasicBotInterface
from dtba.lib.obj.conditions import BaseCondition
from dtba.lib.obj.handlers import BaseHandler
from dtba.lib.obj.handlers import handler_action


class MyCondition(BaseCondition):

    def is_valid(self):
        if 'start' in self.request.message.text:
            return True
        return False


class TestHandler(BaseHandler):

    @handler_action(
        conditions_list=[
            MyCondition
        ]
    )
    def show_menu(self, request):
        print(request.message.chat.id)


class TestBot(BasicBotInterface):

    handlers = [
        TestHandler
    ]