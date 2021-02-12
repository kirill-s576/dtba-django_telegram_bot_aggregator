

class TelegramRequest:

    def __init__(self, bot, call_or_message):
        self.bot = bot
        self.call, self.message = self.__divide_input_message(call_or_message)

    @staticmethod
    def __divide_input_message(call_or_message):
        if hasattr(call_or_message, "message"):
            return call_or_message, call_or_message.message
        else:
            return None, call_or_message


class TextTelegramRequest(TelegramRequest):
    pass


class CallBackTelegramRequest(TelegramRequest):
    pass


class FileTelegramRequest(TelegramRequest):
    pass