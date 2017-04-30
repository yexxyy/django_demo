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
SERVER_HOST='http://119.23.27.133:8102'


#SEND MAIL SETTINGS
EMAIL_HOST='smtp.qq.com'
EMAIL_PORT='25'
EMAIL_HOST_USER='email-help@foxmail.com'
EMAIL_HOST_PASSWORD='afgmlyzhvysxcjjf'
EMAIL_USE_TLS=True