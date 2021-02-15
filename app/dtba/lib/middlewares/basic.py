from abc import ABC, abstractmethod


class BasicMiddleware:

    @abstractmethod
    def process_request(self, request):
        return request