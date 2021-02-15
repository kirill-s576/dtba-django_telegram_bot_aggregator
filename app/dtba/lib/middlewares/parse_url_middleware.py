from .basic import BasicMiddleware

class ParseUrlMiddleware(BasicMiddleware):


    def process_request(self, request):
        request.url = None
        return request