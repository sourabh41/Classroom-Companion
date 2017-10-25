from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class SerializerU(serializers.ModelSerializer):

	class Meta:
		model = User
		#ins = Course.instructor.username
		#fields = '__all__'
		fields = ('username', 'first_name','last_name', )

class SerializerI(serializers.ModelSerializer):
	user = SerializerU(read_only=False)
	class Meta:
		model = Instructor
		#ins = Course.instructor.username
		#fields = '__all__'
		fields = ('user','id')

class Serializer(serializers.ModelSerializer):
	instructor = SerializerI(read_only=False)
	class Meta:
		model = Course
		#ins = Course.instructor.username
		fields = ('id', 'name', 'code', 'instructor')
		#fields = '__all__'

class SerializerQuiz(serializers.ModelSerializer):

	class Meta:
		model = Quiz
		#ins = Course.instructor.username
		fields = ('id', 'number', 'noq', 'course', 'timeout', 'responses')
		#fields = '__all__'

class SerializerQuestion(serializers.ModelSerializer):

	class Meta:
		model = Question
		#ins = Course.instructor.username
		fields = ('id','quiz', 'text', 'option_A', 'option_B', 'option_C', 'option_D')
		#fields = '__all__'


# class SerializerFeedback(serializers.ModelSerializer):

# 	class Meta:
# 		model = Feedback
# 		#ins = Course.instructor.username
# 		fields = ('id','course', 'text', 'date', 'responses')
# 		#fields = '__all__'


class SerializerPoll(serializers.ModelSerializer):

	class Meta:
		model = Poll
		#ins = Course.instructor.username
		fields = ('id','course', 'question', 'date', 'options', 'responses')
		#fields = '__all__'

class SerializerQuery(serializers.ModelSerializer):
	
	class Meta:
		model = Query
		fields = ('id','queries')