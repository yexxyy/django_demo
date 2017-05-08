#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django import forms


admin.site.unregister(User)
admin.site.register(News)
admin.site.register(Banner)
admin.site.register(HouseType)
admin.site.register(Building)
admin.site.register(CollectItem)
admin.site.register(ActivityBanner)


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name','gender','weichat', 'address', 'regions','styles',]

class ProfileInline(admin.StackedInline):
	model = Profile
	form = ProfileForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display=('title','form_link')