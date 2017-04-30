# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-30 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170430_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='news_link',
        ),
        migrations.AddField(
            model_name='banner',
            name='cover',
            field=models.ImageField(default='', upload_to=main.models.pic_upload_path, verbose_name='\u5c01\u9762\u56fe'),
        ),
        migrations.AddField(
            model_name='banner',
            name='detail_url',
            field=models.CharField(default='', max_length=100, verbose_name='\u8be6\u60c5\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='banner',
            name='recommend_id',
            field=models.CharField(blank=True, choices=[('1', '\u4e00\u9897\u661f'), ('2', '\u4e24\u9897\u661f'), ('3', '\u4e09\u9897\u661f'), ('4', '\u56db\u9897\u661f'), ('5', '\u4e94\u9897\u661f')], max_length=10, verbose_name='\u63a8\u8350\u6307\u6570'),
        ),
        migrations.AlterField(
            model_name='building',
            name='location',
            field=models.CharField(blank=True, choices=[('jinjiang', '\u9526\u6c5f'), ('qingyangqu', '\u9752\u7f8a'), ('jinniu', '\u91d1\u725b'), ('wuhou', '\u6b66\u4faf'), ('chenghua', '\u6210\u534e'), ('gaoxing', '\u9ad8\u65b0\u533a'), ('gaoxingxiqu', '\u9ad8\u65b0\u897f\u533a'), ('wenjaing', '\u6e29\u6c5f'), ('shuangliu', '\u53cc\u6d41'), ('longquanyi', '\u9f99\u6cc9\u9a7f'), ('xindu', '\u65b0\u90fd'), ('pixian', '\u90eb\u53bf'), ('dujiangyan', '\u90fd\u6c5f\u5830'), ('qingbaijiang', '\u9752\u767d\u6c5f'), ('pengzhou', '\u5f6d\u5dde'), ('pujiang', '\u6d66\u6c5f'), ('dayi', '\u5927\u9091'), ('xinjin', '\u65b0\u6d25'), ('congzhou', '\u5d07\u5dde'), ('qionglai', '\u909b\u5d03'), ('jintang', '\u91d1\u5802')], max_length=70, verbose_name='\u4f4d\u7f6e'),
        ),
        migrations.AlterField(
            model_name='building',
            name='metro',
            field=models.CharField(blank=True, choices=[('one', '1\u53f7\u7ebf'), ('two', '2\u53f7\u7ebf'), ('three', '3\u53f7\u7ebf'), ('four', '4\u53f7\u7ebf'), ('five', '5\u53f7\u7ebf'), ('seven', '7\u53f7\u7ebf'), ('eight', '\u6210\u704c\u5feb\u901f\u94c1\u8def')], max_length=10, verbose_name='\u5468\u8fb9\u5730\u94c1'),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='house_type',
            field=models.CharField(choices=[('\u4e00\u5c45', '\u4e00\u5c45'), ('\u4e8c\u5c45', '\u4e8c\u5c45'), ('\u4e09\u5c45', '\u4e09\u5c45'), ('\u56db\u5c45', '\u56db\u5c45'), ('\u4e94\u5c45', '\u4e94\u5c45'), ('\u4e94\u5c45\u4ee5\u4e0a', '\u4e94\u5c45\u4ee5\u4e0a')], max_length=10, verbose_name='\u6237\u578b'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='regions',
            field=models.CharField(blank=True, choices=[('jinjiang', '\u9526\u6c5f'), ('qingyangqu', '\u9752\u7f8a'), ('jinniu', '\u91d1\u725b'), ('wuhou', '\u6b66\u4faf'), ('chenghua', '\u6210\u534e'), ('gaoxing', '\u9ad8\u65b0\u533a'), ('gaoxingxiqu', '\u9ad8\u65b0\u897f\u533a'), ('wenjaing', '\u6e29\u6c5f'), ('shuangliu', '\u53cc\u6d41'), ('longquanyi', '\u9f99\u6cc9\u9a7f'), ('xindu', '\u65b0\u90fd'), ('pixian', '\u90eb\u53bf'), ('dujiangyan', '\u90fd\u6c5f\u5830'), ('qingbaijiang', '\u9752\u767d\u6c5f'), ('pengzhou', '\u5f6d\u5dde'), ('pujiang', '\u6d66\u6c5f'), ('dayi', '\u5927\u9091'), ('xinjin', '\u65b0\u6d25'), ('congzhou', '\u5d07\u5dde'), ('qionglai', '\u909b\u5d03'), ('jintang', '\u91d1\u5802')], max_length=10, verbose_name='\u610f\u5411\u533a\u57df'),
        ),
    ]