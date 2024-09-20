# myproject/asgi.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from seat.consumers import SeatConsumer
from seat.routing import websocket_urlpatterns

django.setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})