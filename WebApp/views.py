# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from .forms import *
from .models import *
from django.http import HttpResponse
from django.conf import settings



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.username = user.email
            user.save()
            branch = form.cleaned_data.get('branch')
            ins = Instructor.objects.create(user = user,branch=branch)
            ins.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return auth_views.login
    
        


def home(request):
	if request.user.is_authenticated:
		ins = Instructor.objects.get(user = request.user)
		return render(request,'home.html',{
			'instructor':request.user, 
			'courses':Course.objects.filter(instructor=ins)
			})
	else:
		return HttpResponse("Not Logged in")




