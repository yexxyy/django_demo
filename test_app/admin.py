from django.contrib import admin

# Register your models here.
from test_app.models import User, Book

admin.site.register(User)
admin.site.register(Book)