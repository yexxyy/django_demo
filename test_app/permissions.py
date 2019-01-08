#!/usr/bin/env python
# -*- coding: utf-8 -*-
# permissions.py in django_demo
# Created by yetongxue at 2019-01-08


from rest_framework.permissions import BasePermission
from test_app.models import *


class OwnBookPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user