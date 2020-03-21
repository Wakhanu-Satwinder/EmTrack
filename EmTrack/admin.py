from django.contrib import admin
from .models import Job,Employee,JobHistory

# Register your models here.
#admin.site.register(Job)
#admin.site.register(Employee)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary')
    list_filter = ['hire_date']
    search_fields = ['last_name']
    date_hierarchy = 'hire_date'

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Job)
admin.site.register(JobHistory)