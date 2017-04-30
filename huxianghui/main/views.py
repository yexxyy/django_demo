#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from huxianghui.settings import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, logger
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import base64



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
        profile=Profile(user=user)
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


@csrf_exempt
@require_GET
def signout(request):
    logout(request)
    return HttpResponse('登出成功')


@require_POST
@csrf_exempt
def forget_passwd(request):
    params=request.POST
    try:
        email=params['email']
        user = User.objects.get(email=email)
    except:
        return HttpResponseBadRequest('邮箱不正确')
    if user is not None:
        try:
            subject = '狐享会-重置登录密码'
            link="{}/main/passwd_page/?code={}".format(settings.SERVER_HOST,base64.b64encode(user.username))
            html_message = '<b>重置链接：</b><a href="%s">%s</a>' % (link,link)

            send_mail(
                subject=subject,
                message='',
                from_email='email-help@foxmail.com',  # from
                recipient_list=[user.email,],  # to
                html_message=html_message,
            )
            return HttpResponse('密码重置链接已发送至您的邮箱')
        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest(e)
    return HttpResponseBadRequest('用户不存在')


@require_GET
def passwd_page(request):
    code=request.GET.get('code')
    decode_str=base64.b64decode(code)
    user = User.objects.get(username=decode_str)
    if user is not None:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return render(request, 'reset_passwd.html')
    return HttpResponse('出现了错误')



@csrf_exempt
@require_POST
@login_required
def reset_passwd(request):
    params=request.POST
    user = request.user
    base_string='尊敬的狐享会用户：'
    try:
        password1=params['password1']
        password0=params['password0']
        if len(password0) < 6:
            message = '{}{}'.format(base_string, '密码长度太短')
        elif password0 != password1:
            message = '{}{}'.format(base_string, '两次输入的密码不一致')
        else:
            try:
                user.set_password(password0)
                user.save()
                message = '{}{}'.format(base_string, '密码重置成功')
            except:
                message = '{}{}'.format(base_string, '密码重置失败')
    except:
        message='{}{}'.format(base_string,'参数错误，请重新提交')

    return render(request,'reset_result.html',{'message':message})


@csrf_exempt
@require_POST
@login_required
def change_passwd(request):
    params=request.POST
    user=request.user
    try:
        old_passwd=params['old_passwd']
        password0=params['password0']
        password1 = params['password1']
        user = authenticate(username=user.username, password=old_passwd)
        if user is None:
            return HttpResponseBadRequest('旧密码不正确')
        elif len(password0)<6:
            return HttpResponseBadRequest('密码长度太短')
        elif password0!=password1:
            return HttpResponseBadRequest('两次输入的密码不一致')
        else:
            user.set_password(password0)
            user.save()
            return HttpResponse('密码修改成功')

    except:
        return HttpResponseBadRequest('参数不正确')


#Baner and News
@require_GET
def get_banners(request):
    try:
        banners=Banner.objects.all().order_by('recommend_id')
        json_list=[]
        for banner in banners:
            json_list.append(banner.to_json())
        return JsonResponse({
            'list':json_list,
            'message':'获取banner成功',
        })
    except:
        return HttpResponse('获取banner失败')

@require_GET
def get_news(request):
    try:
        news = News.objects.all()
        json_list = []
        for new in news:
            json_list.append(new.to_json())
        return JsonResponse({
            'list': json_list,
            'message': '获取新闻成功',
        })
    except:
        return HttpResponse('获取新闻失败')




#楼盘展示
@require_GET
def get_buildings(request,page):
    PER_PAGE_NUMBERS=10
    try:
        page_index=int(page)
    except:
        return HttpResponseBadRequest('参数不正确')
    buildings=Building.objects.all().order_by('pk')[PER_PAGE_NUMBERS*(page_index-1):PER_PAGE_NUMBERS*(page_index)]
    json_list=[]
    for building in buildings:
        json_list.append(building.to_json())
    if len(json_list)==0:
        message='暂无更多楼盘信息'
    else:
        message='获取楼盘信息成功'
    return JsonResponse({
        'list':json_list,
        'message':message,
    })



@require_POST
@csrf_exempt
def get_buildings_condition(request):
    params=request.POST
    location = params.get('location')
    area_section= params.get('area_section')
    price_section= params.get('price_section')

    if location and area_section and price_section:
        buildings = Building.objects.filter(location=location,area_section=area_section,price_section=price_section)
    elif location and area_section:
        buildings = Building.objects.filter(location=location, area_section=area_section)
    elif location and price_section:
        buildings = Building.objects.filter(location=location, price_section=price_section)
    elif area_section and price_section:
        buildings = Building.objects.filter(area_section=area_section, price_section=price_section)
    elif location:
        buildings = Building.objects.filter(location=location)
    elif area_section:
        buildings = Building.objects.filter(area_section=area_section)
    elif price_section:
        buildings = Building.objects.filter(price_section=price_section)
    else:
        buildings = Building.objects.all()

    json_list=[]
    for building in buildings:
        json_list.append(building.to_json())

    if len(json_list) == 0:
        message = '此条件下无相关楼盘信息'
    else:
        message = '获取楼盘信息成功'
    return JsonResponse({
        'list':json_list,
        'message':message,
    })


@require_GET
def get_activitys(requset):
    try:
        activitys = Activity.objects.all()
        json_list = []
        for activity in activitys:
            json_list.append(activity.to_json())
        return JsonResponse({
            'list': json_list,
            'message': '获取活动列表成功',
        })
    except:
        return HttpResponse('获取活动列表失败')


@csrf_exempt
@require_GET
def get_collect_items(request,activity_id):
    user=request.user
    try:
        temp_id=int(activity_id)
        activity = Activity.objects.get(pk=temp_id)
        if activity is not None:
            collect_items=activity.collect_item.all()
            json_list=[]
            for item in collect_items:
                json_list.append(item.to_json())
            return JsonResponse({
                'list':json_list,
                'activity_id':temp_id,
                'message':'获取收集字段列表成功'
            })
        else:
            return HttpResponseBadRequest('活动不存在')
    except:
        return HttpResponseBadRequest('参数错误')













