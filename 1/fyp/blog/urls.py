#! -*- coding utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('fyp.blog.views',
    url(r'^$', 'blog_home', name='blog_home'),
    url(r'^(?P<blog_id>\d+)/(?P<slug>[\w-]+)/$', 'blog_detail', name='blog_detail'),
)
