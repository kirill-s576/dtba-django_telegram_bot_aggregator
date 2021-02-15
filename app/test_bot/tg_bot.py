from dtba.lib.obj import BasicBotInterface
from dtba.lib.obj.conditions import BaseCondition
from dtba.lib.obj.handlers import BaseHandler
from dtba.lib.obj.handlers import handler_action

from dtba.lib.obj.conditions import IsText, IsFile, IsCallback, ContainsText, IsNewUser

from dtba.lib.obj.message import TextResponseMessage, ReplyKeyboardResponseMessage

import time
import telebot


class TestHandler(BaseHandler):

    @handler_action(
        conditions_list=[
            IsNewUser,
            IsText,
            ContainsText('start')
        ]
    )
    def show_hi(self, request):
        message = TextResponseMessage(request, "Hello!")
        message.send()
        self.show_menu(request)

    @handler_action(
        conditions_list=[
            IsText,
            ContainsText('menu')
        ]
    )
    def show_menu(self, request):
        message = ReplyKeyboardResponseMessage(request, "Menu!")
        message.add_button("Close")
        request.bot.delete_message(chat_id=request.message.chat.id, message_id=request.message.message_id)
        result = message.send()
        print(result)
        # time.sleep(3)
        # request.bot.edit_message_text(chat_id=request.message.chat.id, message_id=result.message_id, text="тру-ту-ту")

    @handler_action(
        conditions_list=[
            IsText,
            ContainsText('Close')
        ]
    )
    def menu_111(self, request):
        # request.bot.delete_message(chat_id=request.message.chat.id, message_id=request.message.message_id)
        # message = ReplyKeyboardResponseMessage(request, "Menu!")
        # message.send()
        pass


class TestBot(BasicBotInterface):

    handlers = [
        TestHandler
    ]