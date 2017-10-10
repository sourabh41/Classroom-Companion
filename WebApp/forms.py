from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Instructor

class SignUpForm(UserCreationForm):

    branch = forms.CharField( widget=forms.Select(choices=Instructor.BRANCHES))
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2', 'branch')


