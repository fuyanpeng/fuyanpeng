# -*- coding: utf-8 -*-
from django import forms
from fyp.board.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("name", "email", "content",)
        widgets = {
            "name": forms.TextInput(attrs={"class":"textinput"}),
            "email": forms.TextInput(attrs={"class":"textinput"}),
            "content": forms.Textarea(attrs={"class":"content"}),
        }
