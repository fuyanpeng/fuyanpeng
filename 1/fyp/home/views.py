#! -*- coding: utf-8 -*-

from django.shortcuts import render
from fyp.home.models import Links

def index(request):
    links = Links.objects.all()

    return render(request, 'home/index.html',{
        'links': links,
    })

