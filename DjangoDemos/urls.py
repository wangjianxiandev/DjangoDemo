# -*- coding: utf-8 -*-
"""定义DjangoDemos的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),

    # 显示特定的主题页
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #显示新的主题主页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

#     用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 编辑条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),

    url(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic, name='delete_topic')
]