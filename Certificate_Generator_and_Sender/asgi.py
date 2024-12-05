
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Certificate_Generator_and_Sender.settings')

application = get_asgi_application()
