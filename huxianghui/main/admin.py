#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django import forms


# admin.site.register(Profile)
admin.site.unregister(User)
# admin.site.register(LikeRegion)
# admin.site.register(LikeStyle)
admin.site.register(News)
admin.site.register(Banner)
admin.site.register(Building)
admin.site.register(UserLike)


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'phone', 'email', 'gender', 'address', 'regions','styles',]

class ProfileInline(admin.StackedInline):
	model = Profile
	form = ProfileForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

