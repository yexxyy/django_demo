#!/usr/bin/env python
# -*- coding: utf-8 -*-
# urls.py in django_demo
# Created by yetongxue at 2019-01-08


from rest_framework import routers
from django.urls import include, path
from test_app.views import *

router = routers.SimpleRouter()
router.register(r'book', BookViewset)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'register_login/', RegisterLoginView.as_view())
]