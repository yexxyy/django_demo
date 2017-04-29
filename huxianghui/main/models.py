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
    return os.path.join('main/', filename)


GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
)
LOCATIONS=(
    ('qingyang','青羊'),('jinniu','金牛'),('wuhou','武侯'),('chenghua','成华'),('gaoxing','高新区'),('gaoxingxiqu','高新西区'),
    ('wenjaing','温江'),('shuangliu','双流'), ('longqianyi','龙泉驿'),('xindu','新都'),('pixian','郫县'),('dujiangyan','都江堰'),('qingbaijiang','青白江'),
    ('pengzhou','彭州'),('pujiang','浦江'),('dayi','大邑'),('xinjin','新津'),('zongzhou','崇州'),('qonglai','邛崃'),('jintang','金堂')
)
METRO=(
    ('one','1号线'),('two','2号线'),('three','3号线'),('four','4号线'),('five','5号线'),('seven','7号线'),('chengguan','成灌快速铁路'),
)

PRICE_SECTIONS=(
    ('one','3000以下'), ('two','3000-5000'), ('three','5000-7000'), ('four','7000-9000'), ('five','9000-11000'), ('size','11000-15000'), ('seven','15000-20000'),('eight','20000以上'),
)
BUILDING_TYPE=(
    ('one','普通住宅'), ('two','花园洋房'), ('three','别墅'), ('four','商铺'), ('five','写字楼'), ('six','公寓）'),
)
AREA_SECCTIONS=(
    ('one','50㎡以下'), ('two','50-70㎡'), ('three','70-90㎡'), ('four','90-110㎡'), ('five','110-150㎡'), ('six','150-200㎡'), ('seven','200-300㎡'),('eight','300㎡以上'),
)


###################个人中心start##################

# @python_2_unicode_compatible
# class LikeRegion(models.Model):
#     class Meta:
#         verbose_name = '意向区域'
#         verbose_name_plural = '意向区域'
#     region=models.CharField(max_length=10,verbose_name='区域')
#
#     def __str__(self):
#         return self.region
#
#
#
# @python_2_unicode_compatible
# class LikeStyle(models.Model):
#     class Meta:
#         verbose_name = '意向类型'
#         verbose_name_plural = '意向类型'
#     styles=models.CharField(max_length=10,verbose_name='类型')
#
#     def __str__(self):
#         return self.styles


@python_2_unicode_compatible
class Profile(models.Model):
    class Meta:
        verbose_name='用户中心'
        verbose_name_plural = '用户中心'


    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,verbose_name='姓名',null=True,blank=True,default='')
    phone=models.CharField(max_length=11,verbose_name='手机',null=False,)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别', blank=True,null=True)
    address = models.CharField(max_length=50, verbose_name='住址',blank=True,default='')
    regions=models.CharField(max_length=10,choices=LOCATIONS,verbose_name='意向区域',blank=True)
    styles=models.CharField(max_length=10,choices=BUILDING_TYPE,verbose_name='意向类型',blank=True)
    email = models.CharField(max_length=30, verbose_name='邮箱',null=False)

    def __str__(self):
        return self.phone









################### 个人中心结束 ##################


################### Index start ##################
@python_2_unicode_compatible
class News(models.Model):
    class Meta:
        verbose_name='新闻'
        verbose_name_plural='新闻'

    news_img=models.ImageField(
        upload_to=pic_upload_path,
        verbose_name='图片'
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
    news_link=models.ForeignKey(News,on_delete=models.CASCADE)

    def __str__(self):
        return self.news_link.news_name

################### Index end ##################


################### building start ##################
@python_2_unicode_compatible
class Building(models.Model):
    class Meta:
        verbose_name = '楼盘展示'
        verbose_name_plural = '楼盘展示'

    title=models.CharField(max_length=50,verbose_name='标题')
    img=models.ImageField(upload_to=pic_upload_path,verbose_name='图片')
    location=models.CharField(max_length=70,verbose_name='位置')
    phone=models.CharField(max_length=11,verbose_name='电话')
    price=models.FloatField(verbose_name='价格')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class UserLike(models.Model):
    class Meta:
        verbose_name='用户收藏'
        verbose_name_plural='用户收藏'
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    liked=models.ManyToManyField(Building,verbose_name='已收藏',blank=True)

    def __str__(self):
        return self.user.name







################### building end ##################








