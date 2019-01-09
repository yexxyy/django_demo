#!/usr/bin/env python
# -*- coding: utf-8 -*-
# develop.py in django_demo
# Created by yetongxue at 2019-01-07

from demo.settings.settings import *


# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_demo',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'qwerasdf',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
