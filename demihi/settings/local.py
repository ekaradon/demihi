__author__ = 'ekaradon'
from demihi.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# If it sets TEMPLATE_DEBUG to a value that differs from DEBUG, include that value under the 'debug' key in 'OPTIONS'.
# No more useful parameter: TEMPLATE_DEBUG = True

INSTALLED_APPS += (
	# commented while: https://github.com/django-debug-toolbar/django-debug-toolbar/issues/706 is open
	'debug_toolbar',
)

INTERNAL_IPS = ['127.0.0.1']

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

STATIC_ROOT = os.path.join(BASE_DIR, '.static/')
MEDIA_ROOT = os.path.join(BASE_DIR, '.static/media/')
