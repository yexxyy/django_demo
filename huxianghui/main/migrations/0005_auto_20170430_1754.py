# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-30 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170430_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectitem',
            options={'verbose_name': '\u7528\u6237\u586b\u5199\u5b57\u6bb5', 'verbose_name_plural': '\u7528\u6237\u586b\u5199\u5b57\u6bb5'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='recommend_id',
            field=models.IntegerField(verbose_name='\u63a8\u8350\u6307\u6570(\u586b\u5199\uff1a1\u30012\u30013...)'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='recommend_id',
            field=models.IntegerField(verbose_name='\u63a8\u8350\u6307\u6570(\u586b\u5199\uff1a1\u30012\u30013...)'),
        ),
        migrations.AlterField(
            model_name='building',
            name='recommend_id',
            field=models.IntegerField(verbose_name='\u63a8\u8350\u6307\u6570(\u586b\u5199\uff1a1\u30012\u30013...)'),
        ),
    ]
