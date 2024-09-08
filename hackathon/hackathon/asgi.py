import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import seat.routing

# from channels.layers import get_channel_layer #added


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            seat.routing.websocket_urlpatterns
        )
    ),
})

# channel_layer = get_channel_layer() # added!