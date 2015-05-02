__author__ = 'ekaradon'
from demihi.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS += (
	# commented while: https://github.com/django-debug-toolbar/django-debug-toolbar/issues/706 is open
	# 'debug_toolbar',
)