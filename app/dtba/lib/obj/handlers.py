def handler_action(conditions_list: list = []):

    def wrapper(func):
        func.is_action = True
        func.conditions = conditions_list
        return func
    return wrapper


class BaseHandler:

    def __init__(self, request):
        self.request = request
