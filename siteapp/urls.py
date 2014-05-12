from django.conf.urls import patterns, url

from siteapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)