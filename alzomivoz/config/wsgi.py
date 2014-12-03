"""
WSGI config for alzomivoz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")
#from django.core.wsgi import get_wsgi_application

from configurations.wsgi import get_wsgi_application
from dj_static import Cling
 
application = Cling(get_wsgi_application())
