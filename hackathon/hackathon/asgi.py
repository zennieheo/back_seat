# hackathon/asgi.py
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from seat.consumers import SeatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # seat_routing.websocket_urlpatterns
            path('ws/seats/', SeatConsumer.as_asgi()),
        ])
    ),
})