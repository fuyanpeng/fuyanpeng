# -*- coding: utf-8 -*-
from django.contrib import admin

from fyp.blog.models import Category, Entry, Comment, Tag
from fyp.blog.forms import EntryForm


class EntryAdmin(admin.ModelAdmin):
    form = EntryForm

    list_display = ('title', 'tags_name', 'category', 'user')
    list_filter = ('category',)
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'position')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Entry, EntryAdmin)
