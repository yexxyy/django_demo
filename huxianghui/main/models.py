#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from uuid import uuid4

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, Group
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



#图片上传路径
def pic_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('main/', filename)


GENDER_CHOICES = (
    ('男', '男'),
    ('男', '女'),
)
LOCATIONS=(
    ('锦江区', '锦江区'),('青羊区','青羊区'),('金牛区','金牛区'),('武侯区','武侯区'),('成华区','成华区'),
    ('高新区','高新区'),('高新西区','高新西区'),('温江','温江'),('双流','双流'), ('龙泉驿','龙泉驿'),
    ('新都','新都'),('郫县','郫县'),('都江堰','都江堰'),('青白江','青白江'),('彭州','彭州'),
    ('浦江','浦江'),('大邑','大邑'),('新津','新津'),('崇州','崇州'),('邛崃','邛崃'),('金堂','金堂')
)
METRO=(
    ('1号线','1号线'),('2号线','2号线'),('3号线','3号线'),('4号线','4号线'),('5号线','5号线'),('7号线','7号线'),('成灌快速铁路','成灌快速铁路'),
)

PRICE_SECTIONS=(
    ('3000以下','3000以下'), ('3000-5000','3000-5000'), ('5000-7000','5000-7000'), ('7000-9000','7000-9000'),
    ('9000-11000','9000-11000'), ('11000-15000','11000-15000'), ('15000-20000','15000-20000'),('20000以上','20000以上'),
)
BUILDING_TYPE=(
    ('普通住宅','普通住宅'), ('花园洋房','花园洋房'), ('别墅','别墅'), ('商铺','商铺'), ('写字楼','写字楼'), ('公寓','公寓）'),
)
AREA_SECCTIONS=(
    ('50㎡以下','50㎡以下'), ('50-70㎡','50-70㎡'), ('70-90㎡','70-90㎡'), ('90-110㎡','90-110㎡'),
    ('110-150㎡','110-150㎡'), ('150-200㎡','150-200㎡'), ('200-300㎡','200-300㎡'),('300㎡以上','300㎡以上'),
)
HOUSE_TYPE=(
    ('一居','一居'),('二居','二居'),('三居','三居'),('四居','四居'),('五居','五居'),('五居以上','五居以上'),
)
RECOMMADN_IDS=(
    ('1','一颗星'),('2','两颗星'),('3','三颗星'),('4','四颗星'),('5','五颗星')
)


################### building start ##################

@python_2_unicode_compatible
class HouseType(models.Model):
    class Meta:
        verbose_name = '楼盘户型'
        verbose_name_plural = '楼盘户型'
    house_type=models.CharField(max_length=10,verbose_name='户型',choices=HOUSE_TYPE)

    def __str__(self):
        return self.house_type

    def save(self, *args, **kwargs):
        house_types = HouseType.objects.all()
        is_added = False
        for type in house_types:
            if type.house_type == self.house_type:
                is_added = True
        if is_added == False:
            super(HouseType, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Building(models.Model):
    class Meta:
        verbose_name = '楼盘展示'
        verbose_name_plural = '楼盘展示'
    recommend_id = models.IntegerField(verbose_name='推荐指数(填写：1、2、3...)')
    title=models.CharField(max_length=50,verbose_name='标题')
    cover=models.ImageField(upload_to=pic_upload_path,verbose_name='封面图')
    location=models.CharField(max_length=70,verbose_name='位置',choices=LOCATIONS,blank=True)
    metro=models.CharField(max_length=20,verbose_name='周边地铁',choices=METRO,blank=True)
    price_section=models.CharField(max_length=20,verbose_name='价格区间',choices=PRICE_SECTIONS,blank=True)
    house_type=models.ManyToManyField(HouseType,verbose_name='户型')
    building_type=models.CharField(max_length=20,verbose_name='楼盘类型',choices=BUILDING_TYPE,blank=True)
    area_section=models.CharField(max_length=20,verbose_name='面积区间',choices=AREA_SECCTIONS,blank=True)
    open_date=models.DateField(verbose_name='开盘时间')
    detail_url=models.CharField(max_length=100,verbose_name='详情链接')
    phone=models.CharField(max_length=11,verbose_name='联系电话')
    price=models.FloatField(verbose_name='价格(元)')

    def __str__(self):
        return self.title

    def get_cover_url(self):
        return self.cover.url if self.cover else ''

    def to_json(self):
        this = {
            'id': self.pk,
            'title': self.title,
            'cover': self.get_cover_url(),
            'location': self.location,
            'detail_url': self.detail_url,
            'price': self.price,
            'recommend_id': self.recommend_id,
            'phone':self.phone,
        }
        return this


################### building end ##################

###################个人中心start##################


@python_2_unicode_compatible
class Profile(models.Model):
    class Meta:
        verbose_name='用户中心'
        verbose_name_plural = '用户中心'
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,verbose_name='姓名',null=True,blank=True,default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别', blank=True,null=True)
    weichat=models.CharField(verbose_name='微信号',max_length=20,blank=True,null=True)
    address = models.CharField(max_length=50, verbose_name='住址',blank=True,default='')
    regions=models.CharField(max_length=10,choices=LOCATIONS,verbose_name='意向区域',blank=True)
    styles=models.CharField(max_length=10,choices=BUILDING_TYPE,verbose_name='意向类型',blank=True)
    likes=models.ManyToManyField(Building,verbose_name='收藏的楼盘')
    send_reset_password_email=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

################### 个人中心结束 ##################



################### Index start ##################
@python_2_unicode_compatible
class News(models.Model):
    class Meta:
        verbose_name='新闻链接'
        verbose_name_plural='新闻链接'

    news_name=models.CharField(max_length=20,verbose_name='名称',default='')
    news_url = models.CharField(max_length=200, verbose_name='链接', default='')

    def __str__(self):
        return self.news_name

    def to_json(self):
        this={
            'id':self.pk,
            'news_url':self.news_url,
            'news_name':self.news_name,
        }
        return this


@python_2_unicode_compatible
class Banner(models.Model):
    class Meta:
        verbose_name = '顶部广告'
        verbose_name_plural = '顶部广告'

    cover = models.ImageField(upload_to=pic_upload_path, verbose_name='封面图',default='')
    detail_url = models.CharField(max_length=100, verbose_name='详情链接',default='')
    recommend_id = models.IntegerField(verbose_name='推荐指数(填写：1、2、3...)')

    def get_cover_url(self):
        return self.cover.url if self.cover else ''

    def __str__(self):
        return self.get_cover_url()

    def to_json(self):
        this={
            'id':self.pk,
            'cover':self.get_cover_url(),
            'detail_url':self.detail_url,
            'recommend_id':self.recommend_id,
        }
        return this

################### Index end ##################





################### 活动 ##################

COLLECT_ITEMS=(
    ('手机','手机'),('真实姓名','真实姓名'),('年龄','年龄'),('联系地址','联系地址'),
)

class CollectItem(models.Model):
    class Meta:
        verbose_name = '用户填写字段'
        verbose_name_plural = '用户填写字段'
    name=models.CharField(max_length=10,verbose_name='字段名称',choices=COLLECT_ITEMS,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        collect_items=CollectItem.objects.all()
        is_added=False
        for item in collect_items:
            if item.name==self.name:
                is_added=True
        if is_added==False:
            super(CollectItem, self).save(*args, **kwargs)

    def to_json(self):
        this={
            'id':self.pk,
            'name':self.name,
        }
        return this



class ParticipatorInfo(models.Model):
    class Meta:
        verbose_name='参加者信息'
        verbose_name_plural='参加者信息'
    name=models.CharField(max_length=11,verbose_name='姓名',blank=True,null=True)
    phone=models.CharField(max_length=11,verbose_name='手机号码',blank=True,null=True)
    age=models.IntegerField(verbose_name='年龄',blank=True,null=True)
    address=models.CharField(max_length=11,verbose_name='联系地址',blank=True,null=True)
    user=models.ForeignKey(User,related_name='user_info',verbose_name='关联用户')

    def __str__(self):
        return '用户id：{}。报名信息：姓名-{}，手机-{}，年龄-{}，地址-{}'.format(self.user.username,self.name,self.phone,self.age,self.address)



class Activity(models.Model):
    class Meta:
        verbose_name='活动列表'
        verbose_name_plural='活动列表'
    recommend_id=models.IntegerField(verbose_name='推荐指数(填写：1、2、3...)')
    title=models.CharField(max_length=30,verbose_name='标题')
    cover = models.ImageField(upload_to=pic_upload_path, verbose_name='封面图')
    detail_url=models.CharField(max_length=100,verbose_name='详情链接')
    limit_num=models.IntegerField(verbose_name='人数上限')
    collect_item=models.ManyToManyField(CollectItem,verbose_name='请选择您想收集的用户信息')
    participator=models.ManyToManyField(ParticipatorInfo,verbose_name='已报名用户',blank=True)

    def __str__(self):
        return self.title

    def get_cover_url(self):
        return self.cover.url if self.cover else ''

    def to_json(self):
        this={
            'id':self.pk,
            'title':self.title,
            'detail_url':self.detail_url,
            'cover':self.get_cover_url(),
        }
        return this


@python_2_unicode_compatible
class ActivityBanner(models.Model):
    class Meta:
        verbose_name='活动广告'
        verbose_name_plural='活动广告'
    cover= models.ImageField(verbose_name='封面图',upload_to=pic_upload_path,blank=True,default="")
    activity= models.ForeignKey(Activity,on_delete=models.CASCADE)

    def __str__(self):
        return self.activity.title

    def to_json(self):
        if self.cover:
            image_url = self.cover.url
        elif self.activity.cover:
            image_url = self.activity.cover.url
        else:
            image_url = ""
        this={
            "cover":image_url,
            "activity_id": self.activity.pk,
            "title":self.activity.title,
        }
        return this



################### ／活动 ##################


