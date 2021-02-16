from abc import ABC, abstractmethod
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


class ResponseMessage(ABC):

    def __init__(self, request):
        self.request = request


    @abstractmethod
    def send(self):
        pass


class TextResponseMessage(ResponseMessage):

    def __init__(self, request, text):
        self.text = text
        super().__init__(request)

    def send(self):
        return self.request.bot.send_message(chat_id=self.request.message.chat.id, text=self.text)


class InlineMenuButton:

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url


class InlineMenuMessageResponse(ResponseMessage):

    def send(self):
        pass