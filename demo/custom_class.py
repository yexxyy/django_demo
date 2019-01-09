#!/usr/bin/env python
# -*- coding: utf-8 -*-
# custom_class.py in django_demo
# Created by yetongxue at 2019-01-09


from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_query_description = '当前页数'
    page_size_query_param = 'page_size'
    page_size_query_description = '每页数量'