from website.settings.base import *

ALLOWED_HOSTS = ['patrickpages.com', '178.79.131.15']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'label_api',
        'USER': 'label_admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = '/label_api/website/settings/static'

