from django.urls import re_path
from .consumers import SeatConsumer



websocket_urlpatterns = [
    re_path(r'ws/bus/(?P<bus_number>\w+)/$', SeatConsumer.as_asgi()),
]
