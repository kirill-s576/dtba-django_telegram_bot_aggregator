from .request import TelegramRequest
from abc import ABC, abstractmethod


class BaseCondition(ABC):

    def __init__(self, request: TelegramRequest):
        self.request = request

    @abstractmethod
    def is_valid(self):
        pass