#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#个人中心
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
@csrf_exempt
def signup(register):
    return HttpResponse('ok')

