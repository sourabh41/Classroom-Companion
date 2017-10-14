# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BRANCHES = (
        ('CS','Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        )
    branch = models.CharField(null = True,max_length = 2, choices = BRANCHES)



    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BRANCHES = (
        ('CS','Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        )
    branch = models.CharField(null = True,max_length = 2, choices = BRANCHES)
    def __str__(self):
        return self.user.username

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length = 8)
    credits = models.IntegerField(null = True)
    
    def __str__(self):
    	return self.name

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField(null = True)
    noq = models.IntegerField(null = True)
    
    def __str__(self):
        return self.course.name + ' Quiz ' + str(self.number)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    text = models.CharField(max_length = 200, null = True)
    option_A = models.CharField(max_length = 200, null = True)
    option_B = models.CharField(max_length = 200, null = True)
    option_C = models.CharField(max_length = 200, null = True)
    option_D = models.CharField(max_length = 200, null = True)
    response = models.TextField(null = True)
    def __str__(self):
        return self.quiz.course.name + ' Quiz Question '

class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField(null = True)
    date = models.DateField(null = True)
    responses = models.TextField(null = True)
    def __str__(self):
        return self.course.name + ' ' + str(self.date) + ' Feedback '

class Poll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
    question = models.CharField(max_length = 200)
    date = models.DateField(null = True)
    options = models.TextField(null = True)
    responses = models.TextField(null = True)
    def __str__(self):
        return self.course.name + ' ' + str(self.date) + ' Poll '
    