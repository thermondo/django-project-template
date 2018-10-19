"""
WSGI config for testing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.project_name }}.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()

if not settings.DEBUG:
    application = Sentry(application)
