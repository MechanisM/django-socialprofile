"""WSGI File that enables Apache/GUnicorn to run Django"""

# pylint: disable=C0103

import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.pardir), os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)))))

print (sys.path)

from django.core.handlers.wsgi import WSGIHandler
os.environ["DJANGO_SETTINGS_MODULE"] = 'socialprofile_demo.settings'
application = WSGIHandler()