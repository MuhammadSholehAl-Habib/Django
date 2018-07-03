# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Login
from django.shortcuts import render
# Create your views here.

def index(request):
    user_list = Login.objects.order_by('id')
    context = {'user_list' : user_list}
    return render(request, 'index.html', context)

def dashboard(request):
    return render(request, 'maps.html')
