from django.urls import path
from .views import publish_message

urlpatterns = [
    path('publish/', publish_message, name='publish'),
]

from .views import message_list

urlpatterns += [
    path('messages/', message_list, name='message_list'),
]
