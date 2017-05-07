# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-07 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_activitybanner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitybanner',
            options={'verbose_name': '\u6d3b\u52a8\u5e7f\u544a', 'verbose_name_plural': '\u6d3b\u52a8\u5e7f\u544a'},
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='barthday',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u751f\u65e5'),
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='email',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=11, null=True, verbose_name='\u6027\u522b'),
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='id_num',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7'),
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='likes',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u7231\u597d'),
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='wechat',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u5fae\u4fe1\u53f7'),
        ),
        migrations.AddField(
            model_name='participatorinfo',
            name='work',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u804c\u4e1a'),
        ),
        migrations.AlterField(
            model_name='collectitem',
            name='name',
            field=models.CharField(blank=True, choices=[('\u59d3\u540d', '\u59d3\u540d'), ('\u6027\u522b', '\u6027\u522b'), ('\u7535\u8bdd', '\u7535\u8bdd'), ('\u5730\u5740', '\u5730\u5740'), ('\u5fae\u4fe1\u53f7', '\u5fae\u4fe1\u53f7'), ('\u751f\u65e5', '\u751f\u65e5'), ('\u5e74\u9f84', '\u5e74\u9f84'), ('\u90ae\u7bb1', '\u90ae\u7bb1'), ('\u804c\u4e1a', '\u804c\u4e1a'), ('\u7231\u597d', '\u7231\u597d'), ('\u8eab\u4efd\u8bc1\u53f7', '\u8eab\u4efd\u8bc1\u53f7')], max_length=10, verbose_name='\u5b57\u6bb5\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='participatorinfo',
            name='address',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='participatorinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=1, null=True, verbose_name='\u6027\u522b'),
        ),
    ]