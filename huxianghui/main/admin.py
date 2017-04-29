from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Profile)
# admin.site.register(LikeRegion)
# admin.site.register(LikeStyle)
admin.site.register(News)
admin.site.register(Banner)
admin.site.register(Building)
admin.site.register(UserLike)