# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from .forms import *
from .models import *
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.edit import UpdateView
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
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
    else:
        return render(request, 'login.html',{})

def authlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			auth_login(request,user)
			return redirect('home')
		return redirect('login')

def home(request):
	if request.user.is_authenticated:
		ins = Instructor.objects.get(user = request.user)
		return render(request,'home.html',{
			'instructor':request.user, 
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def add_course(request, instructor_id):
	if request.user.is_authenticated:
		ins = Instructor.objects.get(user_id = instructor_id)
		return render(request, 'add_course.html', {
			'instructor': request.user,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def make_course(request):
	if request.user.is_authenticated:
		if request.method =='POST':
			name = request.POST['name']
			code = request.POST['code']
			credits = request.POST['credits']
			newcourse = Course.objects.create(instructor = Instructor.objects.get(user = request.user), name = name, code = code, credits = credits, Feedback = '.')
			newcourse.save()
			return redirect('home')
	else:
		return render(request, 'notloggedin.html',{})

def addstudents(request, course_id):
	if request.user.is_authenticated:
		course = Course.objects.get(id = course_id)
		return render(request, 'addstudents.html',{
			'course': course,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def add_students(request, course_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			course = Course.objects.get(id = course_id)
			file1 = request.FILES['students']
			file1 = file1.read()
			file1 = file1.decode("utf-8").split('\n')[:-1]
			for row in file1:
				row = row.split(',')
				if {'username': row[0]} in User.objects.all().values('username'):
					user = User.objects.get(username = row[0])
					student = Student.objects.get(user = user)
					course.students.add(student)
					course.save()
				elif {'username': row[0]} in Student.objects.filter(course = course):
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
	else:
		return render(request, 'notloggedin.html',{})				

def course_view(request, course_id):
	if request.user.is_authenticated:
		quiz_list = Quiz.objects.filter(course = course_id)
		poll_list = Poll.objects.filter(course = course_id)
		course = Course.objects.get(id = course_id)
		query_list = Query.objects.filter(course = course_id)
		query_titles = {}
		for query in query_list:
			query_title = query.queries.split('~~')[0]
			query_titles[query] = query_title 
			print(query_titles)
		return render(request, 'course_view.html',{
			'course' : Course.objects.get(name = course),
			'quizzes' : quiz_list,
			'polls' : poll_list,
			'query_titles' : query_titles,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def showstudents(request, course_id):
	if request.user.is_authenticated:
		student_list = Student.objects.filter(course = course_id)
		return render(request, 'students.html',{
			'students' : student_list,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def make_poll(request, course_id):
	if request.user.is_authenticated:
		course = Course.objects.get(id = course_id)
		return render(request, 'make_poll.html', {
			'course': course,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def poll(request, course_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			course = Course.objects.get(id = course_id)
			question = request.POST['question']
			date = request.POST['date']
			options = request.POST['options']
			poll = Poll.objects.create(course = course, question = question, date = date, options = options, responses = 'self.')
			poll.save()
		return course_view(request, course_id)
	else:
		return render(request, 'notloggedin.html',{})

def make_quiz(request, course_id):
	if request.user.is_authenticated:
		course = Course.objects.get(id = course_id)
		return render(request, 'makequiz.html', {
			'course': course,
			'id' : course_id,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def quiz(request, course_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			course = Course.objects.get(id = course_id)
			number = int(request.POST['number'])
			numq = int(request.POST['numq'])
			timeout = int(request.POST['timeout'])
			quiz = Quiz.objects.create(course = course, number = number, noq = numq, timeout = timeout, responses = '.')
			quiz.save()
			return render(request, 'addquestions.html', {
				'noq': range(numq),
				'quiz' : quiz,
				'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
				})
	else:
		return render(request, 'notloggedin.html',{})

def addquestions(request, quiz_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			quiz = Quiz.objects.get(id = quiz_id)
			numq = quiz.noq
			for n in range(numq):
				text = request.POST['q'+str(n)]
				option1 = request.POST['a'+str(n)]
				option2 = request.POST['b'+str(n)]
				option3 = request.POST['c'+str(n)]
				option4 = request.POST['d'+str(n)]
				correct = request.POST['co'+str(n)]
				question = Question.objects.create(quiz = quiz, text = text, option_A = option1, option_B = option2, option_C = option3, option_D = option4, correct_option = correct, response = '.')
				question.save()
			return redirect('home')
	else:
		return render(request, 'notloggedin.html',{})


def pollresults(request, poll_id):
	if request.user.is_authenticated:
		poll = Poll.objects.get(id = poll_id)
		options = poll.options.split('\n')
		try:
			responses = poll.responses.split('%')[1:]
		except:
			return render(request, 'noresponsesyet.html', {
				'courses' : Course.objects.filter(instructor = Instructor.objects.get(user = request.user)),
				'course' : poll.course,
				})
		votes = {}
		for option in options:
			option = option.replace("\r", "")
			votes[option] = 0
			print(repr(option))
		for response in responses:
			response = response.split(': ')
			print(repr(response[1]))
			votes[response[1]] = votes[response[1]] + 1
		return render(request, 'pollresults.html', {
			'votes' : votes,
			'poll' : poll,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})


def quizresults(request, quiz_id):
	if request.user.is_authenticated:
		quiz = Quiz.objects.get(id = quiz_id)
		questions = Question.objects.filter(quiz = quiz)
		students = Student.objects.filter(course = quiz.course)
		marks = {}
		for student in students:
			marks[student.user.username] = 0
		for question in questions:
			try:
				print(question.response)
				responses = question.response.split('%')[1:]
			except:			
				return render(request, 'noresponsesyet.html', {
				'courses' : Course.objects.filter(instructor = Instructor.objects.get(user = request.user)),
				'course' : quiz.course,
				})
			for response in responses:
				print(response)
				response = response.split(': ')
				print(response)
				if (response[1] == question.correct_option):
					marks[response[0]] = marks[response[0]] + 1
		return render(request, 'quizresults.html',{
			'quiz' : quiz,
			'marks' : marks,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})


def deletequizzes(request, course_id):
	if request.user.is_authenticated:
		course = Course.objects.get(id = course_id)
		quizzes = Quiz.objects.filter(course = course)
		return render(request, 'deletequizzes.html',{
			'quizzes': quizzes,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def deletequiz(request, quiz_id):
	if request.user.is_authenticated:
		quiz = Quiz.objects.get(id = quiz_id)
		course_id = quiz.course.id
		quiz.delete()
		return course_view(request, course_id)
	else:
		return render(request, 'notloggedin.html',{})

def deletepolls(request, course_id):
	if request.user.is_authenticated:
		course = Course.objects.get(id = course_id)
		polls = Poll.objects.filter(course = course)
		return render(request, 'deletepolls.html',{
			'polls': polls,
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def deletepoll(request, poll_id):
	if request.user.is_authenticated:
		poll = Poll.objects.get(id = poll_id)
		course_id = poll.course.id
		poll.delete()
		return course_view(request, course_id)
	else:
		return render(request, 'notloggedin.html',{})

def FeedbackSubmit(request, key, feedback):
	currentcourse = Course.objects.get(code = key)
	content = getattr(currentcourse, 'Feedback')
	content = content + "%" + feedback
	try:
		Course.objects.filter(code = key).update(Feedback=content)
	except:
		return HttpResponse("Fail")
	return HttpResponse("Success")

def PollSubmit(request, key, feedback):
	currentpoll = Poll.objects.get(id = key)
	content = getattr(currentpoll, 'responses')
	content = content + "%" + feedback
	try:
		Poll.objects.filter(id = key).update(responses=content)
	except:
		return HttpResponse("Fail")
	return HttpResponse("Success")

def viewfeedback(request, course_id):
	if request.user.is_authenticated:
		course = Course.objects.get(id = course_id)
		feedbacks = course.Feedback
		try:
			feedbacks = feedbacks.split('%')[1:]
		except:
			return HttpResponse("No feedbacks yet")
		feedback_list = {}
		for feedback in feedbacks:
			feedback = feedback.split(': ')
			feedback[1] = feedback[1].replace('~~', ": ")
			feedback_list[feedback[0]] = feedback[1]

		return render(request, 'viewfeedback.html', {
			'feedback_list' : feedback_list,
			'course' : course,
			'courses' : Course.objects.filter(instructor = Instructor.objects.get(user = request.user))
			})
	else:
		return render(request, 'notloggedin.html',{})

def QuizSubmit(request, key, feedback):
	feed = feedback.split(": ")
	currentquiz = Quiz.objects.get(id = key)
	con = getattr(currentquiz,'responses')
	con = con + "%" + feed[0]
	Quiz.objects.filter(id = key).update(responses = con)
	feed[1] = feed[1].split("~")
	feed[1] = list(map(lambda option: option.split("-"), feed[1]))
	for option in feed[1]:
		currentques = Question.objects.get(id = option[0])
		content = getattr(currentques, 'response')
		content = content + "%" + feed[0] + ": " + option[1]
		try:
			Question.objects.filter(id = option[0]).update(response=content)
		except:
			return HttpResponse("Fail")
	return HttpResponse("Success")

def make_query(request, key, feedback):
	try:
		course = Course.objects.get(id = key)
		newquery = Query.objects.create(course = course, queries = feedback)
	except:
		return HttpResponse("Fail")
	newquery.save()
	return HttpResponse("Success")

def update_query(request, key, feedback):
	try:
		currentquery = Query.objects.get(id = key)
	except:
		return HttpResponse("Fail")
	content = getattr(currentquery, 'queries')
	content = content + "~~" + feedback
	Query.objects.filter(id = key).update(queries = content)
	return HttpResponse("Success")

def answerquery(request, query_id):
	if request.user.is_authenticated:
		query = Query.objects.get(id = query_id)
		queries = query.queries
		query_title = queries.split('~~')[0]
		queries = queries.split('~~')
		return render(request, 'answerquery.html',{
			'courses':Course.objects.filter(instructor = Instructor.objects.get(user = request.user)),
			'query_title': query_title,
			'query' : query,
			'queries' : queries,
			})
	else:
		return render(request, 'notloggedin.html',{})

def savequery(request, query_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			query = Query.objects.get(id = query_id)
			response = request.POST['response']
			queries = query.queries
			queries = queries + "~~" + "Professor : " + response
			Query.objects.filter(id = query_id).update(queries = queries)
			return answerquery(request, query.id)
	else:
		return render(request, 'notloggedin.html',{})


class queryview(APIView):
	def get(self, request, key):
		try:
			query = Query.objects.filter(course = key)
		except:
			return HttpResponse("No queries for this course")
		serializer = SerializerQuery(query, many = True)
		return Response(serializer.data)

class courseview(APIView):
	def get(self, request, rollno):
		try:
			user = User.objects.get(username = rollno)
		except:
			return HttpResponse("No courses for this roll number")
		student = Student.objects.get(user = user)
		courses = Course.objects.filter(students = student)
		serializer = Serializer(courses, many = True)
		return Response(serializer.data)

class quizview(APIView):
	def get(self, request, key):
		try:
			quiz = Quiz.objects.filter(course = key)
		except:
			return HttpResponse("No courses for this roll number")
		serializer = SerializerQuiz(quiz, many = True)
		return Response(serializer.data)

class questionview(APIView):
	def get(self, request, key):
		try:
			question = Question.objects.filter(quiz = key)
		except:
			return HttpResponse("No courses for this roll number")
		serializer = SerializerQuestion(question, many = True)
		return Response(serializer.data)

class pollview(APIView):
	def get(self, request, key):
		try:
			poll = Poll.objects.filter(course = key)
		except:
			return HttpResponse("No courses for this roll number")
		serializer = SerializerPoll(poll, many = True)
		return Response(serializer.data)
