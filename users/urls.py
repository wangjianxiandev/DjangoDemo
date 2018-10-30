# -*- coding: utf-8 -*-

"""为应用程序users定义url模式"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView


from . import views

urlpatterns = [
    # 登陆界面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销用户
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册界面
    url(r'^register/$', views.register, name='register'),
]