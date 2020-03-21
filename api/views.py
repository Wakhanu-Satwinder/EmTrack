from django.shortcuts import render

# Create your views here.

# api/views.py
from rest_framework import generics,viewsets
from EmTrack.models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('hire_date')

    def  get_serializer_class(self):
    	if self.action=='retrieve':
    		return EmployeeDetailSerializer
    	return EmployeeSerializer	
    	#pass
    #serializer_class = EmployeeSerializer
