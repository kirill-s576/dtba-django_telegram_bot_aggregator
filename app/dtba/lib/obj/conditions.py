from .request import TelegramRequest
from abc import ABC, abstractmethod


class BaseCondition(ABC):

    request: TelegramRequest = None

    @abstractmethod
    def is_valid(self):
        pass


class IsText(BaseCondition):

    def is_valid(self):
        if self.request.__class__.__name__ == "TextTelegramRequest":
            return True
        return False


class IsFile(BaseCondition):

    def is_valid(self):
        if self.request.__class__.__name__ == "FileTelegramRequest":
            return True
        return False


class IsCallback(BaseCondition):

    def is_valid(self):
        if self.request.__class__.__name__ == "CallBackTelegramRequest":
            return True
        return False


class IsNewUser(BaseCondition):

    def is_valid(self):
        if hasattr(self.request, "is_new_user"):
            return self.request.is_new_user
        else:
            return False


class ContainsText(BaseCondition):
    """

    """
    def __init__(self, text: str, ignore_case: bool = True):
        self.text = text
        self.ignore_case = ignore_case

    def is_valid(self):
        if self.ignore_case:
            text = self.text.lower()
            message_text = self.request.message.text.lower()
        else:
            text = self.text
            message_text = self.request.message.text
        if text in message_text:
            return True
        return False
