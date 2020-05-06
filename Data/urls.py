"""Data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from rest_framework import generics,viewsets,routers
from EmTrack import views as EmTrack_views
from django.contrib.auth import views as auth_views
#router = routers.SimpleRouter()
#router.register(r'logout',auth_views.logout)

admin.site.site_header='EmTrack Admin'

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('EmTrack/', include('EmTrack.urls')), # new
    path('',include("django.contrib.auth.urls")),
   
    #path('', include("main.urls")), 
    path('api/', include('api.urls')), # new
    
    #path('login/',EmTrack_views.register,name="login"),
    #path(r'^logout/$',auth_views.logout,name="logout"),
   #url(r'^oauth/', include('social_django.urls', namespace='social')),


]

'''from django.conf.urls import include,url

from EmTrack.models import Employee
from django.views.generic import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict = {
     'queryset': Employee.objects.all(),
}
employee_info = {'model' : Employee}

urlpatterns =('',
     (r'^employees/$', 
          dict(info_dict, template_name='employees/employee_list.html')),
     #(r'^employees/create/$',dict(employee_info,template_name='employees/employee_form.html', post_save_redirect='/employees/')),
     #(r'^employees/update/(?P<object_id>\d+)/$',dict(employee_info, template_name='employees/employee_form.html', post_save_redirect='/employees/')),
     #(r'^employees/delete/(?P<object_id>\d+)/$',  dict(employee_info, template_name='employees/employee_confirm_delete.html',
         # post_delete_redirect='/employees/')),

     (r'^admin/', admin.site.urls),

    # (r'^site_media/(?P.*)$', 'django.views.static.serve',
         # {'document_root': '/home/Data/Data/EmTrack/static'}),
)'''