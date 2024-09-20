# myproject/asgi.py (수정해봄
import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
django_asgi_app = get_asgi_application()
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from seat.consumers import SeatConsumer
from seat.routing import websocket_urlpatterns



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
