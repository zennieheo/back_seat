# your_project_name/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from seat.consumers import SeatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/seats/', SeatConsumer.as_asgi()),
        ])
    ),
})