# 디버그 메세지는 출력하되 외부 서버를 사용
from .base import *

DEBUG = True

# Static
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = os.path.join(ROOT_DIR,'.media')
MEDIA_URL = '/media/'

# uWSGI
WSGI_APPLICATION = 'config.wsgi.application'

secret_db = json.load(open(os.path.join(SECRET_DIR, 'db.json')))

# DB
DATABASES = secret_db['DATABASES']