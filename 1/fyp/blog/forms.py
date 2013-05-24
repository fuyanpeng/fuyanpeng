#-*- coding: utf-8 -*-
from django import forms
from fyp.blog.models import Entry, Comment
from fyp.utils.rte.widgets import KindEditor

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        widgets = {
            'text': KindEditor(attrs={'width': '800px', 'height':'600px'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('nickname', 'content',)
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'nickname'}),
            'content': forms.Textarea(attrs={'class': 'content'}),
        }
