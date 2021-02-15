# Django Telegram Bot Aggregator

This library develops for simple integration Django & Telegram.
Library uses Django 3.* & PyTelegramBotApi libraries.

Main package idea is creation logic same as Django ViewSets with 'request' and Middleware layer.

### Get started:
Create file *tg_bot.py* in django app root.

```python
from dtba.lib.obj import BasicBotInterface
from dtba.lib.obj.handlers import BaseHandler
from dtba.lib.obj.handlers import handler_action
from dtba.lib.obj.conditions import IsText, ContainsText, IsNewUser
from dtba.lib.obj.message import TextResponseMessage


class TestHandler(BaseHandler):

    @handler_action(
        conditions_list=[
            IsNewUser,
            IsText, ContainsText(text="start"),
        ]
    )
    def show_menu(self, request):
        print(request.message.chat.id)
        print(request.message.text)
        print(request.user_model)
        print(request.bot_model)
        message = TextResponseMessage(request, "Hello World!")
        result = message.send()
        print(result)

class TestBot(BasicBotInterface):

    handlers = [
        TestHandler
    ]

```
