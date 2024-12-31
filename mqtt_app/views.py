# from django.shortcuts import render

# # Create your views here.

import json
from django.http import JsonResponse
from mqtt_app.mqtt import client

def publish_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        topic = data.get("topic", "my_home/sensor/device1")
        message = data.get("message", "")
        rc, _ = client.publish(topic, message)
        return JsonResponse({"status": "success", "code": rc})
    return JsonResponse({"error": "Invalid method"}, status=405)

from django.shortcuts import render
from mqtt_app.models import MQTTMessage

def message_list(request):
    messages = MQTTMessage.objects.all().order_by('-received_at')
    return render(request, 'messages.html', {'messages': messages})
