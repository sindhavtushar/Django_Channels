import os
from channels.routing import get_default_application
from django.core.asgi import get_asgi_application
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()

from config.routing import application  # <- must import your routing

# Now 'application' is the ASGI app for Channels
