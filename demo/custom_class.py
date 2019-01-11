#!/usr/bin/env python
# -*- coding: utf-8 -*-
# custom_class.py in django_demo
# Created by yetongxue at 2019-01-09


from rest_framework.pagination import PageNumberPagination
from rest_framework.views import exception_handler


class CustomPageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_query_description = '当前页数'
    page_size_query_param = 'page_size'
    page_size_query_description = '每页数量'


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(exc.detail, list):
            response.data = dict(detail=','.join(exc.detail))
        else:
            response.data = exc.detail
    return response