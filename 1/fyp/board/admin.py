# -*- coding: utf-8 -*-
from django.contrib import admin
from fyp.board.models import Board

class BoardAdmin(admin.ModelAdmin):
    
    model = Board
    list_display = ('name', 'email', 'reply')

admin.site.register(Board, BoardAdmin)

