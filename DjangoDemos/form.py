# -*- coding: utf-8 -*-
from django import forms
from .models import Topic
from .models import Topic, Entry


class TopicForm(forms.ModelForm): # 继承了forms.ModelForm的TopicForm
    class Meta:# 最简单的模板只包含这一个类，告诉Django根据哪个模型创建表单，以及包含 表单的哪个字段
        model = Topic #根据Topic创建一个表单
        fields = ['text'] # 该表单只包含字段text
        labels = {'text': ''} # 让Django不要为text生成标签



class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}

        # widget为html中单行文本，多行文本，或者下拉列表，宽度设置为80列
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}