#-*- coding: utf-8 -*-

PROJECT_APPS = [
    'main.apps.UserCenterConfig',
    'corsheaders',
]

PROJECT_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL=True

AUTH_PROFILE_MODULE = 'main.Profile'

# SERVER_HOST='http://0.0.0.0:8101'
SERVER_HOST='https://www.sohuhxh.com/'


#SEND MAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.qq.com'
EMAIL_PORT='587'
EMAIL_HOST_USER='email-help@foxmail.com'
EMAIL_HOST_PASSWORD='afgmlyzhvysxcjjf'
EMAIL_USE_TLS=True
