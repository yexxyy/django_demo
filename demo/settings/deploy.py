#!/usr/bin/env python
# -*- coding: utf-8 -*-
# deploy.py in django_demo
# Created by yetongxue at 2019-01-07


from demo.settings.settings import *

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', None),
        'HOST':  os.environ.get('MYSQL_HOST', None),
        'USER': os.environ.get('MYSQL_USER', None),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', None)
    }
}
