from .basic import BasicMiddleware


class AddModelsMiddleware(BasicMiddleware):


    def process_request(self, request):
        from ...models import Bot

        bot_model = Bot.objects.get(token=request.bot.token)
        user_model, created = bot_model.get_or_create_user(request.message.chat.id)
        request.bot_model = bot_model
        request.user_model = user_model
        request.is_new_user = created
        return request