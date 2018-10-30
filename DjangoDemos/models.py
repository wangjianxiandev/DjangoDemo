from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键关联到指定主题
    text = models.TextField() # 不限制文字长度
    date_added = models.DateTimeField(auto_now_add=True) # 按照创建顺序呈现条目，并在每个条目旁放置时间戳

    class Meta: # 我们在实体类中嵌套了Meta类储存管理模型的额外信息使用entries返回多个条目
        verbose_name_plural = 'entries'


    def __str__(self):
        """返回模型字符串表示"""
        return self.text[:50] + "..."