from settings import *


INSTALLED_APPS=BASE_INSTALLED_APPS+PROJECT_APPS
MIDDLEWARE_CLASSES=BASE_MIDDLEWARE_CLASSES+PROJECT_MIDDLEWARE


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # mysql database setting:
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huxianghui_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '',
        'PORT': 3306,
        'OPTIONS': {

        }
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = '/Users/yetongxue/Desktop/assets_upload'