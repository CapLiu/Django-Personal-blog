# -*- coding=utf-8 -*-
from django.shortcuts import render
from users.models import Users
from blogs.models import Blog

def index(request):
    try:
        username = request.session['username']
        user = Users.objects.get(username=username)
    except KeyError:
        user = Users.objects.get(username='anony')
    except Users.DoesNotExist:
        user = Users.objects.get(username='anony')
    blogList = Blog.objects.filter(draft=False).order_by('title')
    # username = request.session.get('username')
    content = { 'blog_list':blogList,
                'curruser':user
               }
    return render(request, 'myblog/index.html', content)