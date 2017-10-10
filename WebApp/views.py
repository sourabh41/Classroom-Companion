# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from .models import Instructor
from django.contrib.auth import login as auth_login
from django.http import HttpResponse



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.username = "i:" + user.email
            user.save()
            branch = form.cleaned_data.get('branch')
            ins = Instructor.objects.create(user = user,branch=branch)
            ins.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
	return render(request,'login.html',{})


