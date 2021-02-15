import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

BOT_ID = 1

from dtba.models import Bot


bot = Bot.objects.get(id=BOT_ID)
bot.start_polling()