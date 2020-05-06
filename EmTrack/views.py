import pandas as pd
import numpy as np
import csv 
import sqlalchemy
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response,redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Avg,Min,Max,Sum
from bokeh.plotting import figure,output_file,show
from .static.fusioncharts.fusioncharts import FusionCharts
from bokeh.embed import components
from .models import Employee,Job
#from sqlalchemy import create_engine
import psycopg2 as pg
import pandas.io.sql as psql
#engine=create_engine('postgresql://user@localhost:5432/sqlalchemy')
#from bokeh.server import server
#from . import bk_config
#from bokeh.models import ColumnDataSource,FactorRange
#from bokeh.palletes import Spectra16
#from bokeh.transform import factor_cmap
from django.contrib.messages import constants as message_constants  
from .models import Employee
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from .forms import RegisterForm,ContactForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib.auth.decorators import login_required
#from . import helpers

from django.core.mail import send_mail
from .forms import CustomUserCreationForm,ContactForm
from collections import OrderedDict


class EmployeeListView(ListView):
    model = Employee
    template_name = 'pages/employee_list.html'

class BlockListView(ListView):
    model = Employee
    template_name = 'pages/blocklist.html'


 #DISPLAYING ON VIEWS PAGE
@login_required(login_url='login')
def views(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Available Jobs and their maximum salary",
        "captionFont":"Arial",
        "captionFontColor":"Blue",
        "captionFontBold":"1",
            "subCaption": "County Government",
            "subCaptionFont":"Arial",
            "subCaptionFontColor":"#Red",
            "subCaptionFontBold":"0",
            "xAxisName": "Job Title",
            "yAxisName": "Max_salary (In Ksh)",
            "exportEnabled":"1",
            #"numberPrefix": "Kshs.",
            "theme": "Gamme1"
        }
    
    dataSource["data"] = []
    # Iterate through the data in `Emplo` model and insert in to the `dataSource['data']` list.
    for key in Job.objects.all():
        data = {}
        data['label'] = key.job_title
        data['value'] = key.max_salary
        dataSource['data'].append(data)
    pie2D = FusionCharts("pie2D", "ex1" , "400", "300", "chart-1", "json", dataSource)
    line= FusionCharts("line", "ex2" , "400", "300", "chart-2", "json", dataSource)

#displaying column bar on the views page
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Employees Basic salary",
        "captionFont":"Arial",
        "captionFontColor":"Green",
        "captionFontBold":"1",
            "subCaption": "County Government",
            "subCaptionFont":"Arial",
            "subCaptionFontColor":"#Red",
            "subCaptionFontBold":"0",
            "xAxisName": "Employee",
            "yAxisName": "Salary in (ksh)",
            "exportEnabled":"1",
            #"font":"Times New Roman",
            #"numberPrefix": "Kshs.",
            "theme": "carbon"
        }
    

    dataSource["data"] = []
    # Iterate through the data in `Emplo` model and insert in to the `dataSource['data']` list.
    for key in Employee.objects.all():
        data = {}
        data['label'] = key.first_name
        data['value'] = key.salary
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    
    
    column2D = FusionCharts("column2D", "ex3" , "400", "300", "chart-3", "json", dataSource)
    return render_to_response('pages/views.html', {'output': pie2D.render(),'output2': line.render(),'output3': column2D.render()})

#FOR DISPLAYING COLUMN GRAPH TO CHARTS PAGE
@login_required(login_url='login')
def charts(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {

        "caption": "Available Jobs and their maximum salary",
        "captionFont":"Arial",
        "captionFontColor":"#993300",
        "captionFontBold":"1",
            "subCaption": "County Government",
            "subCaptionFontColor":"blue",
            "xAxisName": "Job Title",
            "yAxisName": "Max_salary (In Ksh)",
            "exportEnabled":"1",
            "enableLegend":"1",
            #"numberPrefix": "Kshs.",
            "theme": "gammel"
        }
 
    dataSource["data"] = []
    # Iterate through the data in `Job` model and insert in to the `dataSource['data']` list.
    for key in Job.objects.all():
        data = {}
        data['label'] = key.job_title
        data['value'] = key.max_salary
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    
    column2D = FusionCharts("column2D", "ex2" , "400", "300", "chart-3", "json", dataSource)
    return render_to_response('pages/charts.html', {'output': column2D.render()})


#FOR DISPLAYING COLUMN GRAPH TO HOME PAGE
@login_required(login_url='login')
def home(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.

    return render_to_response('pages/home.html',{})
def account(request):

    return render_to_response('pages/account.html',{})	



#...
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'pages/register.html', {'form': f})


#New Login
def login(request):
    #if request.user.is_authenticated():
      
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            request.session['username'] = username
            messages.success(request,'Login successfull')
            return redirect('profile')
 
        else:
            messages.error(request,'Error wrong username/password')
 
    return render_to_response('Registration/login.html',{})
@login_required(login_url='login')
def profile(request):
    '''if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)''' 
    messages.success(request,'Login successfull')
    return render(request, 'pages/profile.html', {})
    '''else:
        return render(request, 'Registration/login.html', {})'''
 
@login_required(login_url='login') 
def signout(request):
    auth.logout(request)
    try:
        del request.session['username']
        request.session.flush()
    except:
        messages.info(request,"You Logged out Successfully")
        return render(request,"Registration/logout.html",{})
    #return HttpResponse("<strong>You are now logged out.</strong")


#COMPUTATIONS
@login_required(login_url='login')
def comp(response):
    connection = pg.connect("host='localhost' dbname=Datadb user=postgres password=staminah@8")
    q=Employee.objects.all().aggregate(Avg('salary'))
    p=Employee.objects.all().aggregate(Min('salary'))
    r=Employee.objects.all().count()
    s=Job.objects.all().count()
    t=Employee.objects.all().aggregate(Max('salary'))
    u=Employee.objects.all().aggregate(Sum('salary'))
    #t=Employee.objects.filter(employee_id=['']).values('first_name','last_name')

    #
    return render(response,"pages/computations.html",{"output":q,"output2":p,"output3":r,"output4":s
    	,"output5":t,"output6":u})

#CONTACT PAGE Original
'''@login_required(login_url='login')
def contact_us(request):
    if request.method=='POST':
    	form=ContactForm(request.POST)
    	if form.is_valid():
    			#send email code goes here
    		sender_name=form.cleaned_data['name']
    		sender_email=form.cleaned_data['email']
            #message=form.cleaned_data[message]
    		message="{0} has sent you a new message:\n\n{1}".format(sender_name,form.cleaned_data['message'])
    		send_mail('New Enquiry',message,sender_email,['windersonrolles@gmail.com'])

    	#return HttpResponse('Thanks For Contacting Us!')
    	return render(request,"pages/contact-us.html",{'form':form})
    else:
    	form=ContactForm()
    return render(request,'pages/contact-us.html',{'form':form})'''

@login_required(login_url='login')
def about(request):
    return render(request,'pages/about.html',{})
    
    			
'''def raw(response):
    connection = pg.connect("host='localhost' dbname=Datadb user=postgres password=staminah@8")
    #dataframe = psql.read_sql_query
    #query=("SELECT * FROM employees WHERE employee_id=employee_id",connection)
    q=Employee.objects.all().filter('employee_id')

    return render(response,'pages/raw.html',{'output':q})'''
def feedback(request):
    return render_to_response('pages/feedback.html',{})


'''@login_required(login_url='login')
def contact_us(request):
    name=''
    email=''
    message=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        message=form.cleaned_data.get("message")

        if request.user.is_authenticated:
            subject= str(request.user) + "'s Comment"
        else:
            subject= "A Visitor's Comment"


        message= name ,'+', " with the email, " ,'+', email,'+', ", sent the following message:\n\n" ,'+', message;
        send_mail(subject, message,email,['windersonrolles@gmail.com'])


        context= {'form': form}

        return render(request, 'pages/contact-us.html', context)

    else:
        context= {'form': form}
        return render(request, 'pages/contact-us.html', context)'''
'''def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')'''
 
@login_required(login_url='login') 
def contact_us(request):
    submitted =False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
           
             # assert False
            #return HttpResponseRedirect('contact/?submitted=False')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'pages/contact-us.html', {'form': form, 'submitted': submitted}) 