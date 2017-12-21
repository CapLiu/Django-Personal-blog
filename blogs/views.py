# -*- coding=utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog,Comment,Category,Users
from django.urls import reverse
from django.core.exceptions import ValidationError
import datetime
from .blogForm import BlogForm

# Create your views here.

def content(request,blogId):
    blog = Blog.objects.get(id=blogId)
    comment = Comment.objects.filter(attachedblog=blog)
    request.session['currblogId'] = blogId
    blog_title = blog.title
    blog_content = blog.content
    blogContent = {
                   'blog_title':blog_title,
                   'content':blog_content,
                   'comment_list':comment
                   }
    blog.readcount+=1
    blog.save()
    return render(request,'blogs/content.html',blogContent)


# def saveBlog(request):
#     blog_title = request.POST['blogtitle']
#     blog_category = request.POST['category']
#     blog_content = request.POST['blogcontent']
#     auther = Users.objects.get(username=request.session['username'])
#     category = Category.objects.get(categoryname=blog_category)
#     result_info = ''
#     try:
#         myblog = Blog.create(blog_title,auther,category,blog_content,datetime.datetime.now(),datetime.datetime.now())
#         myblog.save()
#         category.blogcount = category.blogcount+1
#         category.save()
#         result_info = 'Success'
#     except ValidationError as e:
#         result_info = 'Fail'
#     return HttpResponseRedirect(reverse('blogs:addblogResult', kwargs={'info': result_info}))


def saveComment(request):
    comment_content = request.POST['blogcomment']
    blog = Blog.objects.get(pk=request.session['currblogId'])
    result_info = ''
    try:
        auther = Users.objects.get(username=request.session['username'])
    except KeyError:
        auther = Users.objects.get(username='anony')
    try:
        mycomment = Comment.create(blog,comment_content,auther,datetime.datetime.now())
        mycomment.save()
        result_info = 'Success'
    except ValidationError as e:
        result_info = 'Fail'
    return HttpResponseRedirect(reverse('blogs:content',kwargs={'blog_id':request.session['currblogId']}))


def addBlog(request):
    if request.method == 'POST':
        tmpBlog = Blog.objects.get(id=request.session['currentblogId'])
        if tmpBlog:
            form = BlogForm(request.POST,instance=tmpBlog)
            tmpBlog = form.save(commit=False)
            tmpBlog.draft = False
            tmpBlog.save()
            result_info = 'Success'
        else:
            form = BlogForm(request.POST)
            if form.is_valid():
                newBlog = form.save(commit=False)
                newBlog.auther = Users.objects.get(username=request.session['username'])
                newBlog.draft = False
                category = Category.objects.get(categoryname=newBlog.category)
                category.blogcount = category.blogcount+1
                category.save()
                newBlog.save()
                result_info = 'Success'
        del request.session['currentblogId']
        return HttpResponseRedirect(reverse('blogs:addblogResult', kwargs={'info': result_info}))
    else:
        form = BlogForm()
    return render(request, 'blogs/addblog.html', {'form':form})


def addBlogResult(request,info):
    tipMessage=''
    if info == 'Success':
        tipMessage = '博文已成功发表！'
    else:
        tipMessage = info
    parameters = {'info':tipMessage}
    return render(request, 'blogs/addblogResult.html', parameters)


def saveDraft(request):
    if request.method == 'POST':
        blogId = request.session.get('currentblogId','-1')
        if blogId!='-1':
            try:
                tmpBlog = Blog.objects.get(id=blogId)
                form = BlogForm(request.POST, instance=tmpBlog)
                tmpBlog = form.save(commit=False)
                tmpBlog.draft = True
                tmpBlog.save()
                result_info = u'文章已保存于草稿箱中。'
                return HttpResponse(result_info)
            except Blog.DoesNotExist:
                form = BlogForm(request.POST)
                if form.is_valid():
                    newBlog = form.save(commit=False)
                    newBlog.auther = Users.objects.get(username=request.session['username'])
                    category = Category.objects.get(categoryname=newBlog.category)
                    category.blogcount = category.blogcount+1
                    category.save()
                    newBlog.save()
                    request.session['currentblogId'] = newBlog.id
                    result_info = u'文章已保存于草稿箱中。'
                    return HttpResponse(result_info)
                return HttpResponse('test')
        else:
            form = BlogForm(request.POST)
            if form.is_valid():
                newBlog = form.save(commit=False)
                newBlog.auther = Users.objects.get(username=request.session['username'])
                category = Category.objects.get(categoryname=newBlog.category)
                category.blogcount = category.blogcount + 1
                category.save()
                newBlog.save()
                request.session['currentblogId'] = newBlog.id
                result_info = u'文章已保存于草稿箱中。'
                return HttpResponse(result_info)
            else:
                return HttpResponse('test')
    else:
        return HttpResponse('test')