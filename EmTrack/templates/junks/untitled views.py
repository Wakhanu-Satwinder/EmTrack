from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView
from .models import Employee
from bokeh.plotting import figure,output_file,show
from bokeh.embed import components


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'


'''class Registration(Register):
 	"""docstring for ClassName"""
 	
 	def __init__(self, arg):
 		super(Registration, self).__init__()
 		self.arg = arg
 		return render(request,"register.html")'''
 		 
 	

def employee_list(request):
 	return render(request,"employee_list.html")	

def homepage(request):
 
 #Graph X and Y cordinates
 x=[1,2,3,4,5]
 y=[1,2,3,4,5]
#setting up graph plot for displaying the graph
 plot=figure(title='Line Graph',x_axis_label='X-Axis',y_axis_label='Y-Axis',plot_width=400,plot_height=400)
 #plot line
 plot.line(x,y, line_width=2)
 #store components
 script,div=components(plot)
#return to django homepage with components sent as arguments which will then be displayed

 #return render(request, 'pages/base.html', {})
 return render_to_response('pages/base.html', {'script':script,'div':div})
 

 ###################OTHER JUNKS
 '''def raw(request):
    connection = pg.connect("host='localhost' dbname=Datadb user=postgres password=staminah@8")
    dataframe = psql.read_sql_query("SELECT first_name,salary FROM employees",connection)
    pd=psql.DataFrame(Employee.objects.all())
    return HttpResponse(dataframe.to_html('pages/raw.html'),{})
  
def showemployees(request):
	Employees=Employee.objects
	return render(request,'pages/all.html',{'Employees':Employees})'''


'''class EmployeeDetailView(DetailView):
	model=Employee
	template_name = 'detaiil.html'
	Employee.objects.filter(first_name=first_name)'''


'''def getfile(request):
     response=HttpResponse(content_type='text/csv')
     response['Content-Disposition']='attachment;filename="employees.csv"'
     employees=Employee.objects.all()
     writer=csv.writer(response)
     for employee in employees:
         writer.writerow([employee.employee_id,employee.first_name,employee.last_name,employee.phone_number,
             employee.hire_date,employee.salary])
         return render_to_response(request,'templates/pages/detail.html')'''

'''def detail(request):
     connection = pg.connect("host='localhost' dbname=Datadb user=postgres password=staminah@8")
     dataframe = psql.read_sql_query("SELECT first_name,salary FROM employees",connection)
     records=cursor.fetchall()
     #dataframe = psql.DataFrame("SELECT * FROM category", connection)
     #df = pd.read_sql_query('select * from employees',con=connection)
     db_cursor=connection.cursor()
     io=open('copy_to.csv',w)
     cursor.copy_to('COPY records TO io')
    
     io.close()
     print(dataframe)
     #template_name='pages/details.html'
     return render_to_response('pages/details.html',{})'''

 '''class Registration(Register):
     """docstring for ClassName"""
     
     def __init__(self, arg):
         super(Registration, self).__init__()
         self.arg = arg
         return render(request,"register.html")'''
#FOR BOKEH

 def homepage(request):
    
 
 #Graph X and Y cordinates
 x=[1,2,3,4,5]
 y=[1,2,3,4,5]
#output_file=("pages/base.html",mode="cdn")
#setting up graph plot for displaying the graph
 plot=figure(title='Line Graph',x_axis_label='X-Axis',y_axis_label='Y-Axis',plot_width=400,plot_height=400)
 #plot line
 plot.line(x,y,line_width=2)
 #store components
 script,div=components(plot)   
#show(plot)
#return to django homepage with components sent as arguments which will then be displayed

 #return render(request, 'pages/base.html', {})
 return render_to_response( 'pages/base.html', {'script':script,'div':div} )


 #FOR CARDVIEW CATEGORY
 <!--categories widget-->
        <!--<div class="card my-4 bg-dark  text-white" id="categories">
            <h5 class="card-header">Computations</h5>
              <div class="card-body">
                <div class="row">
                   <div class="col-lg-6">
                     <ul class="list-unstyled mb-0">
                       <li>
                        <a href="#">Social</a>
                       </li>
                       <li>
                        <a href="#"> Finance</a>
                       </li>
                       <li>
                        <a href="#">Blockchain</a>
                       </li>
                     </ul>
                    
                   </div>
                    
                </div>
                
              </div>
        </div>-->
        