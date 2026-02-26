import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
import apps.echo.routing
import apps.livecalculator.routing
import apps.chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

django.setup()

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": ASGIStaticFilesHandler(django_asgi_app),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.echo.routing.websocket_urlpatterns +
            apps.livecalculator.routing.websocket_urlpatterns +
            apps.chat.routing.websocket_urlpatterns
        )
    ),
})
