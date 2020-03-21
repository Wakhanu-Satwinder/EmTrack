from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email=forms.EmailField()
	password1=forms.CharField(max_length=10)
	password1=forms.CharField(max_length=10)
	'''class meta:
		model=User
		fields=["username","email","password1","password2"]'''


class LoginForm(AuthenticationForm):
	email=forms.EmailField()
	password1=forms.CharField()
	'''class meta:
		model=User
		fields=["username","password1"]'''

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
   
		
		