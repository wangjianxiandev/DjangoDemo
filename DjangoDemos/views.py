from django.shortcuts import render
from .models import Topic, Entry
from django.urls import reverse
from django.http import  HttpResponseRedirect
from .form import TopicForm
from .form import EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """学习笔记的主页"""
    return render(request, 'DjangoDemos/index.html')


@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('data_added') # 用户只能看到自己的主题
    # topics = Topic.objects.order_by('data_added')
    context = {'topics':topics}
    return render(request, 'DjangoDemos/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'DjangoDemos/topic.html', context)

@login_required
def new_topic(request):
    """添加新的主题"""
    if request.method != 'POST': # 测试确定请求是 POST还是GET,GET方法返回一个空表单

         """未提交数据：创建一个新表单"""
         form = TopicForm() # 创建一个TopicForm， 由于TopicForm没有指定任何参数，Django将创建一个空表单
    else:
        """POST提交数据：创建一个新表单"""
        form =  TopicForm(request.POST) # POST的数据存储request.POST
        if form.is_valid(): # 要将提交的信息保存到数据库，必须先通过确定他们是有效的， is_valid核实用户填写了所有必不可少的字段
            new_topic = form.save(commit=False) # 将表单数据写入数据库
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('DjangoDemos:topics'))# 使用reverse()获取页面topics的url, 并将它传递给HttpResponseRedirect(重定向到页面topics)

    context = {'form': form} # 将变量存储在formz中，并通过上下文字典
    return render(request, 'DjangoDemos/new_topic.html', context)

    context = {'form': form} # 将变量存储在formz中，并通过上下文字典


@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    else:
        topic.delete()
        return HttpResponseRedirect(reverse('DjangoDemos:topics'))

@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)


    if request.method != 'POST':
        '''未提交数据'''
        form = EntryForm()
    else:
        '''POST提交数据，对数据进行处理'''
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('DjangoDemos:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'DjangoDemos/new_entry.html', context)


@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    else:
        entry.delete()
        return HttpResponseRedirect(reverse('DjangoDemos:topic', args=[topic.id]))



@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('DjangoDemos:topic',args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'DjangoDemos/edit_entry.html', context)





