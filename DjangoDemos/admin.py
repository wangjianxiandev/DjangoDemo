from django.contrib import admin

# Register your models here.

from DjangoDemos.models import Topic, Entry

# 向管理网站注册Topic

admin.site.register(Topic)
admin.site.register(Entry)