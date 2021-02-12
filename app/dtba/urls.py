from django.urls import path
from .views import bot_webhook


urlpatterns = [
    path('bot_webhook/<token>', bot_webhook, name="bot_webhook")
]
