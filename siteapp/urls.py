from django.conf.urls import patterns, url

from siteapp import views

urlpatterns = patterns('',
	#ex:/blog
    url(r'^blog/$', views.blog_post_list, name='blog'),
	#ex:/blog/some-title-text
	url(r'^blog/(?P<slug>.*)$', views.blog_post_detail, name='blog_detail'),
    url(r'^$', views.index, name='index')
)