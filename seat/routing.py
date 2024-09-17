# seat/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/seats/', consumers.SeatConsumer.as_asgi()),
]