from django.db import models
from .bot import Bot


class BotUser(models.Model):

    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=50)

    current_url = models.CharField(max_length=1024, null=True, blank=True)

