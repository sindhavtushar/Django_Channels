from django.urls import path
from .consumers import LiveCalculatorConsumer

websocket_urlpatterns = [
    path("ws/livecalc/", LiveCalculatorConsumer.as_asgi()),
]