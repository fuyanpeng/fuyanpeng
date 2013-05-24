#! -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from fyp.blog.models import Category, Entry, Comment, Tag
from fyp.blog.forms import CommentForm 

def blog_home(request):
    
    categories = Category.objects.all()
    ###分类显示###
    cate = request.REQUEST.get('category',None)
    if cate is not None:
        category = Category.objects.get(slug=cate)
        entries = category.entry_set.all()
    else:
        category = None
        entries = Entry.objects.all()
    
    ###搜索###
    search = request.REQUEST.get('s', None)
    if search is not None:
        entries = Entry.objects.filter(title__icontains=search)

    ###最新的十条评论###
    newcomments = Comment.objects.all().order_by("-created_at")[:10]

    ###所有的标签###
    tags = Tag.objects.all()

    ###按标签显示###
    tag_id = request.REQUEST.get('tag', None)
    if tag_id is not None:
        tag = Tag.objects.get(pk=tag_id)
        entries = tag.entry_set.all()
    try:
        tag_id = int(tag_id)
    except:
        pass
    return render(request, 'blog/blog.html',{
        
        'category': category,
        'categories': categories,
        'entries': entries,
        'newcomments': newcomments,
        'tags': tags,
        'highlight': tag_id,
    })

def blog_detail(request, blog_id, slug):
    
    categories = Category.objects.all()
    entry = Entry.objects.get(pk=blog_id)
    entry.click_count += 1
    entry.save()
    
    ###最新的十条评论
    newcomments = Comment.objects.all().order_by("-created_at")[:10]

    ###所有的标签
    tags = Tag.objects.all()

    comments = entry.comment_set.all()
    for k,comment in enumerate(comments):
        comment.floor = k+1
    
    try:
        prev_blog = Entry.objects.filter(category=entry.category, id__lt=entry.id)[0]
    except:
        prev_blog = None

    try:
        next_blog = Entry.objects.filter(category=entry.category, id__gt=entry.id).order_by('created_at')[0]
    except:
        next_blog = None 

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.entry = entry
            comment.save()
            return redirect(request.path+"#comment")
        pass
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html',{
        
        'entry': entry,
        'categories': categories,
        'prev_blog': prev_blog,
        'next_blog': next_blog,
        'comments': comments,
        'newcomments':newcomments,
        'form': form,
        'tags': tags,
    })


def blog_search(request):
    
    return render(request, 'blog/blog_search.html', {
    
    })
