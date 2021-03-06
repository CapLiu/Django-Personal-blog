from django.conf.urls import url,include
from . import views
from myblog.views import index

app_name='users'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^userregister/$',views.userregister,name='userregister'),
    url(r'^userlogin/$',views.userlogin,name='userlogin'),
    url(r'^loginResult/(?P<info>.*)$',views.loginResult,name='loginResult'),
    url(r'^registerResult/(?P<info>.*)$',views.registerResult,name='registerResult'),
    url(r'^logoff/$',views.logoff,name='logoff'),
    url(r'^userindex/(?P<username>.*)$',views.userIndex,name='userIndex'),
    url(r'^userinfo/(?P<username>.*)$',views.userinfo,name='userinfo')
]