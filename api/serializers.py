from rest_framework import serializers

from EmTrack.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('last_name', 'email', 'job', 'hire_date','salary')

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name','last_name', 'email', 'job', 'hire_date','salary')
	
		