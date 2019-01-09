from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from test_app.filters import *
from test_app.serializers import *
from test_app.permissions import OwnBookPermission
from rest_framework.permissions import IsAuthenticated
from demo.custom_class import CustomPageNumberPagination


class BookViewset(viewsets.ModelViewSet):
    """
    list: Book列表
        ---
        ordering: price create_time author__birthday
    retrieve: Book详情
    create: 创建Book
    update: 更新Book
    partial_update: 更新Book部分信息
    delete: 删除Book
    """
    queryset = Book.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_class = BookFilterSet
    serializer_class = BookSerializer
    http_method_names = ('patch', 'delete', 'post', 'get')
    ordering_fields = ('price', 'create_time', 'author__birthday')

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'partial_update':
            permissions = (IsAuthenticated, OwnBookPermission)
        else:
            permissions = ()
        return [p() for p in permissions]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return BookCreateSerializer
        return BookSerializer