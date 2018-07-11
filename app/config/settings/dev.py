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
WSGI_APPLICATION = 'config.wsgi.dev.application'

secret_db = json.load(open(os.path.join(SECRET_DIR, 'db.json')))

# DB
DATABASES = secret_db['DATABASES']
print(DATABASES)


# django-storages
INSTALLED_APPS +=[
    'storages',
]
# S3 Burket UPload
DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

# DB PostgreSQL Access
AWS_ACCESS_KEY_ID = secret_db["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = secret_db["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = secret_db["AWS_STORAGE_BUCKET_NAME"]
AWS_DEFAULT_ACL = secret_db["AWS_DEFAULT_ACL"]
AWS_S3_REGION_NAME = secret_db["AWS_S3_REGION_NAME"]
AWS_S3_SIGNATURE_VERSION = secret_db["AWS_S3_SIGNATURE_VERSION"]

