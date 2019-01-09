#!/usr/bin/env python
# -*- coding: utf-8 -*-
# serializers.py in django_demo
# Created by yetongxue at 2019-01-08


from test_app.models import *
from rest_framework.serializers import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'avatar', 'birthday')


class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ('create_time',)

    author = PrimaryKeyRelatedField(queryset=User.objects.all(), help_text='User id')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 2

    author = UserSerializer()