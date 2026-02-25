from django.urls import path
from django.urls import re_path
from .consumers import EchoConsumer, BingoConsumer

websocket_urlpatterns = [
    path("ws/echo/", EchoConsumer.as_asgi()),
    re_path(r'ws/bingo/(?P<room_name>\w+)/$', BingoConsumer.as_asgi()),
]