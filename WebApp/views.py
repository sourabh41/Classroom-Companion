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

import csv
import codecs


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

def add_course(request):
	if request.user.is_authenticated:
		ins = Instructor.objects.get(user = request.user)
		return render(request, 'add_course.html', {
			'instructor': request.user,
			})

def make_course(request):
	if request.user.is_authenticated:
		if request.method =='POST':
			name = request.POST['name']
			code = request.POST['code']
			credits = request.POST['credits']
			newcourse = Course.objects.create(instructor = Instructor.objects.get(user = request.user), name = name, code = code, credits = credits)
			newcourse.save()
			return redirect('add_course')

def add_students_to_course1(request):
	if request.user.is_authenticated:
		ins = Instructor.objects.get(user = request.user)
		return render(request, 'selectcourse.html',{
			'courses':Course.objects.filter(instructor = ins)
			})

def add_students_to_course2(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			code = request.POST['code']
			course = Course.objects.get(code = code)
			file1 = request.FILES['students']
			# csvf.open()
			# csvf = csvf.split('\n')[:-1]
			# for row in csvf:
			# 	row = row.split(',')
			# 	if {'username': row[0]} in User.objects.all().values('username'):
			# 		continue
				# else:
				# 	print("asd")
				# 	user = User.objects.create_user(username = row[0],password = row[0])
				# 	user.first_name = row[1]
				# 	user.last_name = row[2]
				# 	user.save()
				# 	branch = course.Instructor.branch
				# 	student = Student.objects.create(user = user, branch = branch)
				# 	student.save()
				# 	course.students.add(student)
				# 	course.save()
				# 	return HttpResponse(row[0])
			file1 = file1.read()
			file1 = file1.decode("utf-8").split('\n')[:-1]
			for row in file1:
				row = row.split(',')
				if {'username': row[0]} in User.objects.all().values('username'):
					continue
				else:
					user = User.objects.create_user(username = row[0],password = row[0])
					user.first_name = row[1]
					user.last_name = row[2]
					user.save()
					instructor = Instructor.objects.get(user = request.user)
					branch = instructor.branch
					student = Student.objects.create(user = user, branch = branch)
					student.save()
					course.students.add(student)
					course.save()
			return redirect('home')				
			
		# 	csvfile = request.FILES['students']
		# 	dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
		# 	csvfile.open()
		# 	reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
		# return HttpResponse(reader)

def course_view(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			ins = Instructor.objects.get(user = request.user)
			code = request.POST['code']
			course = Course.objects.get(code = code)
			polls = Poll.objects.filter(course = course)
			quizzes = Quiz.objects.filter(course = course)
			return render(request, 'course_view.html')  

