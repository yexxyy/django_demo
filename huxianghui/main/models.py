#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from uuid import uuid4

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, Group


#图片上传路径
def pic_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('records/', filename)




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
@python_2_unicode_compatible
class News(models.Model):
    class Meta:
        verbose_name='新闻'
        verbose_name_plural='新闻'

    news_img=models.ImageField(
        upload_to=pic_upload_path,
        verbose_name='链接'
    )
    news_name=models.CharField(max_length=20,verbose_name='名称',default='')

    def __str__(self):
        return self.news_name

    def get_imgurl(self):
        return self.news_img.url if self.news_img else ''


@python_2_unicode_compatible
class Banner(models.Model):
    class Meta:
        verbose_name = '顶部广告'
        verbose_name_plural = '顶部广告'
    newslink=models.ForeignKey(News,on_delete=models.CASCADE)

    def __str__(self):
        return self.newslink