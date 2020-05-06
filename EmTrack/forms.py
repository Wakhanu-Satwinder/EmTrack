from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render

#Original
'''class RegisterForm(UserCreationForm):
	email=forms.EmailField()
	password1=forms.CharField(max_length=10)
	password2=forms.CharField(max_length=10)
	class meta:
		model=User
		fields=["username","email","password1","password2"]'''


class CustomUserCreationForm(forms.Form): 
    username = forms.CharField(label='Username', min_length=4, max_length=15)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class LoginForm(AuthenticationForm):
    '''email=forms.EmailField()'''
    username = forms.CharField(label='Username', min_length=4, max_length=10)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    '''password1=forms.CharField(widget=forms.PasswordInput())
	class meta:
		model=User
		fields=["username","password1"]'''

'''class ContactForm(forms.Form):
    name=forms.CharField(max_length=100, label="Name")
    email=forms.EmailField( label="Email")
    message=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':30}))
   

class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))
class ContactForm(forms.Form):
    
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':30}), required=True)	'''	

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':30}), required=True)
		