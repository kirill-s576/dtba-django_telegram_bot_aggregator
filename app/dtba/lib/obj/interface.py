import telebot
import inspect

from .request import TextTelegramRequest
from .request import FileTelegramRequest
from .request import CallBackTelegramRequest

from ..middlewares import AddModelsMiddleware
from ..middlewares import ParseUrlMiddleware


class BasicBotInterface:
    """

    """

    custom_middlewares = []

    __middlewares = [
        AddModelsMiddleware,
        ParseUrlMiddleware,

    ] + custom_middlewares

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
            request = self.__process_middlewares(request)
            self.__process_handlers(request)

        @bot.message_handler(func=lambda message: True, content_types=['document', 'audio', 'photo'])
        def file_message_handler(message):
            request = FileTelegramRequest(bot, message)
            request = self.__process_middlewares(request)
            self.__process_handlers(request)

        @bot.callback_query_handler(func=lambda call: True)
        def call_message_handler(call):
            request = CallBackTelegramRequest(bot, call)
            request = self.__process_middlewares(request)
            self.__process_handlers(request)

        return bot

    def __process_handlers(self, request):
        for handler in self.handlers:
            inited_handler = handler(request)
            methods = inspect.getmembers(inited_handler, predicate=inspect.ismethod)
            for method in methods[1:]:
                func = getattr(inited_handler, method[0])
                if 'is_action' in func.__dict__:
                    condition_flag = True
                    for condition in func.__dict__["conditions"]:
                        try:
                            inited_condition = condition()
                        except TypeError:
                            inited_condition = condition
                        condition = inited_condition
                        condition.request = request
                        if not condition.is_valid():
                            condition_flag = False
                    if condition_flag:
                        func(request)
                        break

    def __process_middlewares(self, request):
        for middleware in self.__middlewares:
            request = middleware().process_request(request)
        return request