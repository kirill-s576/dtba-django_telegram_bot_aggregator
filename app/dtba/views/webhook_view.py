from django.views.decorators.csrf import csrf_exempt
from ..models import Bot
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


@csrf_exempt
def bot_webhook(request, token):
    """ Handler for Webhook from telegram """
    bot = get_object_or_404(Bot, token=token)
    if request.method == "POST":
        try:
            json_string = request.body.decode("utf-8")

            return JsonResponse({"success": True}, status=200)
        except:
            return JsonResponse({"success": False}, status=500)
    else:
        return JsonResponse({"bot_name": bot.name})
