from website.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'releases',                      
        'USER': 'patrick',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}