__author__ = 'ekaradon'
from demihi.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['demihi.fr']

SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'


STATIC_ROOT = os.path.expanduser('~/static/demihi/')
MEDIA_ROOT = os.path.expanduser('~/media/demihi/')
COMPRESS_ROOT = os.path.join(STATIC_ROOT)
