from django.contrib import admin
from .models import Bot
from .models import BotUser


admin.site.register(Bot)
admin.site.register(BotUser)
