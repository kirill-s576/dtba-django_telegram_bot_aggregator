from abc import ABC, abstractmethod
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


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


class ReplyKeyboardResponseMessage(TextResponseMessage):

    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)

    def add_button(self, text):
        self.keyboard.row(
            KeyboardButton(text=text)
        )

    def send(self):
        keyboard = self.keyboard
        if len(keyboard.keyboard) == 0:
            keyboard = ReplyKeyboardRemove()
        return self.request.bot.send_message(chat_id=self.request.message.chat.id,
                                             text=self.text,
                                             reply_markup=keyboard)

    # def remove(self):
    #     return self.request.bot.edit_message_text(chat_id=self.request.message.chat.id,
    #                                          text="Mennu!",
    #                                          message_id=76, reply_markup=ReplyKeyboardRemove())