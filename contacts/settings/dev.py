from .base import *

DEBUG = True

LANGUAGE_CODE = 'fr-be'

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)  # Used by app debug_toolbar

from .local import *
