import telebot
from .request import TextTelegramRequest
import inspect


class BasicBotInterface:
    """

    """
    middlwares = [

    ]

    handlers = [

    ]

    def __init__(self, token):
        self.token = token

    @property
    def bot(self) -> telebot.TeleBot:
        bot = telebot.TeleBot(self.token)
        bot = self.__basic_middleware(bot)
        return bot

    def __basic_middleware(self, bot):

        @bot.message_handler(func=lambda message: True)
        def text_message_handler(message):
            request = TextTelegramRequest(bot, message)
            self.__process_handlers(request)

        @bot.message_handler(func=lambda message: True, content_types=['document', 'audio', 'photo'])
        def file_message_handler(message):
            print(message.text)

        @bot.callback_query_handler(func=lambda call: True)
        def call_message_handler(call):
            print(call.message.text)

        return bot

    def __process_handlers(self, request):
        for handler in self.handlers:
            inited_handler = handler(request)
            methods = inspect.getmembers(inited_handler, predicate=inspect.ismethod)
            for method in methods[1:]:
                func = getattr(inited_handler, method[0])
                if 'is_action' in func.__dict__:
                    for condition in func.__dict__["conditions"]:
                        init_condition = condition(request)
                        if init_condition.is_valid():
                            func(request)
