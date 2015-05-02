__author__ = 'ekaradon'
from demihi.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
	# commented while: https://github.com/django-debug-toolbar/django-debug-toolbar/issues/706 is open
	'debug_toolbar',
)

INTERNAL_IPS = ['127.0.0.1']

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)