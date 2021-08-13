from django.contrib import admin
from django.contrib.admin.sites import site
from FeedApp.models import Post, Report

# Register your models here.

admin.site.register(Post)
admin.site.register(Report)