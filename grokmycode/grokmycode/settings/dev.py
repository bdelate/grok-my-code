import psycopg2
from .base import *


DEBUG = True

SECRET_KEY = 'j0k3hn*+)5oi0p(3xqkg$tj!fvpfs$u=$)ypolrb93ldavsmy='

ADMIN_URL = 'admin/'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '',
    }
}
