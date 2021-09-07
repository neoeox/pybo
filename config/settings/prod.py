from .base import *

ALLOWED_HOSTS = ['3.38.83.218']

STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'h7C=V~umnp^(!l?6ShW|DW7p+xk%d7[x',
        'HOST': 'ls-ae8ad19ba139ad391e9b69915f11af2696be5b35.cwyax3kmmqbo.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

