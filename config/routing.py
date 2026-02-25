from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import apps.echo.routing
import apps.livecalculator.routing

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.echo.routing.websocket_urlpatterns +
            apps.livecalculator.routing.websocket_urlpatterns
        )
    ),
})
