#! -*- coding utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('fyp.board.views',
    url(r'^$', 'board', name='board'),
)
