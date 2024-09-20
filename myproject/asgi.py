import os

from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import seat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": URLRouter(seat.routing.websocket_urlpatterns)
    }
)
