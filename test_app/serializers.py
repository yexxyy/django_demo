#!/usr/bin/env python
# -*- coding: utf-8 -*-
# serializers.py in django_demo
# Created by yetongxue at 2019-01-08


from test_app.models import *
from rest_framework.serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.exceptions import *


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


class RegisterLoginSerializer(Serializer):
    username = CharField(max_length=20, help_text='用户名')
    password = CharField(max_length=64, min_length=8, help_text='密码')
    is_login = BooleanField(help_text='是否是登录')

    def is_valid(self, raise_exception=False):
        super(RegisterLoginSerializer, self).is_valid(raise_exception)
        username = self.validated_data['username']
        password = self.validated_data['password']
        is_login = self.validated_data['is_login']
        if is_login:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("用户名或密码错误")
        else:
            user = User.objects.filter(username=username).first()
            if user:
                raise ValidationError("已注册")
            user = User.objects.create_user(username=username, email=None, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return token.key