from dtba.lib.obj import BasicBotInterface
from dtba.lib.obj.conditions import BaseCondition
from dtba.lib.obj.handlers import BaseHandler
from dtba.lib.obj.handlers import handler_action

from dtba.lib.obj.conditions import IsText, IsFile, IsCallback, ContainsText, IsNewUser

from dtba.lib.obj.message import TextResponseMessage

import telebot


class MainMenu(BaseHandler):

    @handler_action(
        conditions_list=[
            IsCallback
        ]
    )
    def root(self, request):
        pass


class TestBot(BasicBotInterface):

    handlers = [
        {"url": "/", "handler": MainMenu}
    ]