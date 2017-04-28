#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, Group


###################个人中心start##################

@python_2_unicode_compatible
class LikeRegion(models.Model):
    region=models.CharField(max_length=10,verbose_name='区域')

    def __str__(self):
        return self.region



@python_2_unicode_compatible
class LikeStyle(models.Model):
    styles=models.CharField(max_length=10,verbose_name='类型')

    def __str__(self):
        return self.styles


@python_2_unicode_compatible
class Profile(models.Model):
    class Meta:
        verbose_name='用户中心'
        verbose_name_plural = '用户中心'


    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,verbose_name='姓名')
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别', blank=True)
    address = models.CharField(max_length=50, verbose_name='住址', blank=True)
    regions=models.ManyToManyField(LikeRegion,verbose_name='意向区域',blank=True)
    styles=models.ManyToManyField(LikeStyle,verbose_name='意向类型',blank=True)
    email = models.CharField(max_length=30, verbose_name='邮箱')


    def __str__(self):
        return self.name









###################个人中心结束##################


###################start##################