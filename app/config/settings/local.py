# 외부 연결이 없어도 프로젝트를 실행할 수 있도록
from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.amazonaws.com',
]

# Static
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = os.path.join(ROOT_DIR,'.media')
MEDIA_URL = '/media/'

# uWSGI
WSGI_APPLICATION = 'config.wsgi.application'

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

