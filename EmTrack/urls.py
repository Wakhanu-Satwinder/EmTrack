# books/urls.py
from django.urls import path,include
from .views import EmployeeListView,views,home,charts,comp,account,contact_us,about,register,login,BlockListView,signout,profile
from . import views




urlpatterns = [
    path('emp/', EmployeeListView.as_view(),name='employees'),
    #path('employees/',views.EmployeeViewSet),
    path('block/', BlockListView.as_view()),
    #path('registration/',Registration.as_view()),
    #path('det/', views.EmployeeDetailView.as_view(),name='detail'),
    #path('det/', views.emp_list, name='emplist'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('home/', views.home, name='home'),
    path('views/', views.views, name='views'),
    path('charts/', views.charts, name='charts'),
    path('calc/', views.comp, name='calc'),
    path('account/', views.account, name='account'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    #path('raw/', views.raw, name='raw')
    #path('all/', views.showemployees, name='showemployees')

   
]