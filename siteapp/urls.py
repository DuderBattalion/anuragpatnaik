from django.conf.urls import patterns, url

from siteapp import views

urlpatterns = patterns('',
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^$', views.index, name='index')
)