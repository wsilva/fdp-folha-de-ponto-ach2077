import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ach2077',
        'USER': 'root',
        'PASSWORD': 'tom',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
