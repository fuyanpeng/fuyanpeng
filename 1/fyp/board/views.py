# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from fyp.board.models import Board
from fyp.board.forms import BoardForm

def board(request):
    messages = Board.objects.all()
    
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = BoardForm()

    return render(request, 'board/board.html',{
    
        'messages':messages,
        'form':form,
    })
