from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['phone']),
            models.Index(fields=['email']),
        ]

    nickname = models.CharField(max_length=20, help_text='昵称')
    avatar = models.URLField(max_length=500, null=True, blank=True, help_text='头像')
    birthday = models.DateField(null=True, blank=True, help_text='生日')
    country = models.CharField(max_length=20, null=True, blank=True, help_text='国家')
    city = models.CharField(max_length=20, null=True, blank=True, help_text='城市')
    phone = models.CharField(max_length=11, null=True, blank=True, help_text='电话')
    email = models.EmailField(null=True, blank=True, help_text='邮箱')
    address = models.CharField(max_length=200, null=True, blank=True, help_text='地址')


class Book(models.Model):
    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = ('-create_time',)

    name = models.CharField(max_length=20, help_text='书名')
    author = models.ForeignKey(User, on_delete=True, related_name='books', help_text='作者')
    price = models.FloatField(default=0, help_text='价格,默认0')
    create_time = models.DateTimeField(auto_created=True)