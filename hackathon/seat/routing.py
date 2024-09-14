# seat/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/seats/', consumers.SeatConsumer.as_asgi()),
]
