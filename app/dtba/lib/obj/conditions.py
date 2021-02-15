from .request import TelegramRequest
from abc import ABC, abstractmethod


class BaseCondition(ABC):

    def __init__(self, request: TelegramRequest=None, **kwargs):
        self.request = request
        for key, value in kwargs.items():
            setattr(self, key, value)

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