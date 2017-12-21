from django.conf.urls import url
from . import views
from django.conf.urls import include
from users import urls as userurls



app_name='blogs'
urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^(?P<blogId>[0-9]*)$', views.content, name='content'),
    url(r'^addblog/$', views.addBlog, name='addblog'),
    # url(r'^saveblog/$',views.saveBlog,name='saveBlog'),
    url(r'^addblogResult/(?P<info>.*)$', views.addBlogResult, name='addblogResult'),
    url(r'^saveComment/$',views.saveComment,name='saveComment'),
    url(r'^saveDraft/$',views.saveDraft,name='saveDraft')


]