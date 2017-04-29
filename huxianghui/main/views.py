#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


#个人中心
@require_POST
@csrf_exempt
def signup(request):
    params=request.POST
    try:
        phone=params['phone']
        email=params['email']
        password=params['password']
        password2=params['password2']
    except:
        return HttpResponseBadRequest('参数不正确')
    if len(password)<6:
        return HttpResponseBadRequest('密码位数不够')
    elif password!=password2:
        return HttpResponseBadRequest('密码不一致')
    elif len(phone)!=11:
        return HttpResponseBadRequest('手机号码不正确')
    elif len(email)==0:
        return HttpResponseBadRequest('邮箱为空')
    try:
        user=User.objects.create_user(username=phone,password=password,email=email)
        profile=Profile(user=user,phone=phone,email=email)
        profile.save()
        print 'success!'
    except:
        return HttpResponseBadRequest('注册失败')
    return HttpResponse('注册成功')


@require_POST
@csrf_exempt
def signin(request):
    params=request.POST
    try:
        phone=params['phone']
        password=params['password']
    except:
        HttpResponseBadRequest('参数不正确')

    user=authenticate(username=phone,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponse('登录成功')
        else:
            return HttpResponseBadRequest('账号未激活')
    return HttpResponseBadRequest('账号或密码不对')



@require_GET
def signout(request):
    logout(request)
    return HttpResponse('登出成功')