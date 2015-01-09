import os
from django.conf import settings

DEBUG=False
TEMPLATE_DEBUG=False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config(default='postgres://user:pass@host/db')
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
# DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
