from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Instructor

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name..'}), required=True)
	# last_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name..'}), required=True)
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email..'}), required=True)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password..'}),required = True)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password..'}),required = True)
	branch = forms.ChoiceField( choices=Instructor.BRANCHES, widget=forms.Select(attrs={'placeholder': 'Select branch..','class':'Dropdown'}),required = True)

	class Meta:
		model = User
		fields = ( "first_name", "last_name", "email", "password1", "password2", "branch")