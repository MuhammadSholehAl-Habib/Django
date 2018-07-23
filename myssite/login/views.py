# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.http import HttpResponseRedirect
from .models import Login, marker, siapsat, organization, ekko
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .serializers import markerSerializer, siapsatSerializer, organizationSerializer, ekkoSerializer
# Create your views here.

def index(request):
    user_list = Login.objects.order_by('id')
    context = {'user_list' : user_list}
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

# def dashboard(request):
#     marker_list = siapsat.objects.order_by('id')
#     ekko_list = ekko.objects.order_by('id')
#     organization_list = organization.objects.order_by('id')
#     context = {'marker_list' : marker_list,'ekko_list' : ekko_list, 'organization_list' : organization_list }
#     return render(request, 'maps.html', context)

def dashboard(request):
    siapsat_list = siapsat.objects.all();
    context = {'siapsat_list':siapsat_list};
    return render(request, 'maps.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'signup.html' , context)

class markerView(viewsets.ModelViewSet):
    queryset = marker.objects.all()
    serializer_class = markerSerializer

class siapsatView(viewsets.ModelViewSet):
    queryset = siapsat.objects.all()
    serializer_class = siapsatSerializer

class organizationView(viewsets.ModelViewSet):
    queryset = organization.objects.all()
    serializer_class = organizationSerializer

class ekkoView(viewsets.ModelViewSet):
    queryset = ekko.objects.all()
    serializer_class = ekkoSerializer

def listView(request):
    data = marker.objects.all()
    return render(request, 'test.html', {"sr":data} )
