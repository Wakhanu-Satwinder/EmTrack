import pandas as pd
import numpy as np
import csv 
import sqlalchemy
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, render_to_response,redirect
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
from .forms import RegisterForm,ContactForm,LoginForm
from django.core.mail import send_mail

class EmployeeListView(ListView):
    model = Employee
    template_name = 'pages/employee_list.html'

class BlockListView(ListView):
    model = Employee
    template_name = 'pages/blocklist.html'


 #DISPLAYING ON VIEWS PAGE
def views(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Available Jobs and their maximum salary",
        "captionFont":"Arial",
        "captionFontColor":"Blue",
        "captionFontBold":"1",
            "subCaption": "County Government",
            "xAxisName": "Job Title",
            "yAxisName": "Max_salary (In Ksh)",
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
    pie2D = FusionCharts("pie2D", "ex1" , "300", "200", "chart-1", "json", dataSource)
    line= FusionCharts("line", "ex2" , "300", "200", "chart-2", "json", dataSource)

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
    
    
    column2D = FusionCharts("column2D", "ex3" , "300", "200", "chart-3", "json", dataSource)
    return render_to_response('pages/views.html', {'output': pie2D.render(),'output2': line.render(),'output3': column2D.render()})

#FOR DISPLAYING COLUMN GRAPH TO CHARTS PAGE
def charts(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Available Jobs and their maximum salary",
        "captionFont":"Arial",
        "captionFontColor":"#993300",
        "captionFontBold":"1",
            "subCaption": "County Government",
            "xAxisName": "Job Title",
            "yAxisName": "Max_salary (In Ksh)",
            #"numberPrefix": "Kshs.",
            "theme": "Gamme1"
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
def home(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.

    return render_to_response('pages/home.html',{})	

	
#FOR USER REGISTRATION FORMS	
def register(request):
    if request.method== "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect("login")
    else:
        form=RegisterForm()
        return render(request,"pages/register.html",{"form":form})
#FFOR USER LOGIN
def login(request):
    if request.method== "POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #messages=form.cleaned_data['message']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request,user)
                messages.info(request,"You Are Now logged in as {username}")
                #return render(request,"pages/base.html",context={"form":form})
                return redirect("home")
            '''else:
                messages.error(request,"Invalid username or password")
            form.save()
            home(request, user)'''  
    else:
        messages.error(request,"Invalid username or password")
        form=LoginForm()
        return render(request,"Registration/login.html",context={"form":form})

#COMPUTATIONS
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

#CONTACT PAGE
def contact_us(response):
    if response.method=='POST':
    	form=ContactForm(response.POST)
    	if form.is_valid():
    			#send email code goes here
    		sender_name=form.cleaned_data['name']
    		sender_email=form.cleaned_data['email']
            #message=form.cleaned_data[message]
    		message="{0} has sent you a new message:\n\n{1}".format(sender_name,form.cleaned_data['message'])
    		send_mail('New Enquiry',message,sender_email,['windersonrolles@gmail.com'])

    	#return HttpResponse('Thanks For Contacting Us!')
    	return render(response,"pages/contact-us.html",{'form':form})
    else:
    	form=ContactForm()
    return render(response,'pages/contact-us.html',{'form':form})

def about(request):
    return render(request,'pages/about.html',{})
    
    			
'''def raw(response):
    connection = pg.connect("host='localhost' dbname=Datadb user=postgres password=staminah@8")
    #dataframe = psql.read_sql_query
    #query=("SELECT * FROM employees WHERE employee_id=employee_id",connection)
    q=Employee.objects.all().filter('employee_id')

    return render(response,'pages/raw.html',{'output':q})'''