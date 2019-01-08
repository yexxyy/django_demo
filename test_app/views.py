from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from test_app.filters import *
from test_app.serializers import *
from test_app.permissions import OwnBookPermission
from rest_framework.permissions import IsAuthenticated


class BookViewset(viewsets.ModelViewSet):
    """
    list: Book列表
    retrieve: Book详情
    create: 创建Book
    update: 更新Book
    partial_update: 更新Book部分信息
    delete: 删除Book
    """
    queryset = Book.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = BookFilterSet
    serializer_class = BookSerializer
    http_method_names = ('patch', 'delete', 'post', 'get')

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'partial_update':
            permissions = (IsAuthenticated, OwnBookPermission)
        else:
            permissions = ()
        return [p() for p in permissions]