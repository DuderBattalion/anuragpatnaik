from django.conf.urls import patterns, url

from siteapp import views

urlpatterns = patterns('',
    url(r'^blog/$', views.blog_post_list, name='blog'),
    url(r'^$', views.index, name='index')
)