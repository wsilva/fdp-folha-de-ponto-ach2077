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

# INSTALLED_APPS += ('storages',)
# AWS_STORAGE_BUCKET_NAME = "fdp_bucket_name"
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = S3_URL