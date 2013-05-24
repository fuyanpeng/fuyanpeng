# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class KindEditor(forms.Textarea):

    class Media:
        css = {
            'all': (
                '/static/editor/kindeditor-4.1.2/themes/default/default.css',
                '/static/editor/kindeditor-4.1.2/plugins/code/prettify.js',
            ),
        }
        js  = (
            '/static/editor/kindeditor-4.1.2/kindeditor.js',
            '/static/editor/kindeditor-4.1.2/plugins/code/prettify.js',
        )

    def __init__(self, attrs={}, **kwargs):
        super(KindEditor, self).__init__(attrs)
        self.width = kwargs.pop('width', 800)
        self.height = kwargs.pop('height', 400)

    def render(self, name, value, attrs=None):
        rendered = super(KindEditor, self).render(name, value, attrs)
        context = {
            'name': name,
            'width': self.width,
            'height': self.height,
            'STATIC_URL': settings.STATIC_URL,
            'UPLOAD_JSON': reverse('kindeditor_upload')
        }
        return rendered + mark_safe(render_to_string('editor/kindeditor.html', context))
