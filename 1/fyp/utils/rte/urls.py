# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from fyp.utils.rte.views import kindeditor_upload


urlpatterns = patterns('',
    url(r'^upload/$', kindeditor_upload, name='kindeditor_upload'),
)
