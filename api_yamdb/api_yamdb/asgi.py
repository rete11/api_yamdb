<<<<<<< HEAD
"""
ASGI config for YaMDb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

=======
>>>>>>> 0da0ef7b50be21e3e6f5d2cff8297ddb80370de2
import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
=======

>>>>>>> 0da0ef7b50be21e3e6f5d2cff8297ddb80370de2
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')

application = get_asgi_application()
