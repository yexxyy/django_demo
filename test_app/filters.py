#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filters.py in django_demo
# Created by yetongxue at 2019-01-08

import django_filters
from test_app.models import *


class BookFilterSet(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ('name', 'price_min', 'price_max')

    name = django_filters.CharFilter(help_text='检索书名', method='filter_name')
    price_min = django_filters.NumberFilter(help_text='Book最低价', method='filter_price_min')
    price_max = django_filters.NumberFilter(help_text='Book最高价', method='filter_price_max')

    def filter_name(self, queryset, name, value):
        return queryset.filter(name__contains=value)

    def filter_price_min(self, queryset, name, value):
        return queryset.filter(price__gte=value)

    def filter_price_max(self, queryset, name, value):
        return queryset.filter(price__lte=value)