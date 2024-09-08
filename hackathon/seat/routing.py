from django.urls import re_path
from .consumers import SeatConsumer, TestConsumer



websocket_urlpatterns = [
    re_path(r'ws/bus/(?P<bus_number>\w+)/$', SeatConsumer.as_asgi()),

    re_path(r'ws/websocket-test/$', TestConsumer.as_asgi()),
]
