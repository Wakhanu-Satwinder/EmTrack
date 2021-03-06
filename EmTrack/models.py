from django.db import models

# Create your models here.
class Job(models.Model):
    job_id = models.CharField(max_length=10, primary_key=True)
    job_title = models.CharField(max_length=35)
    min_salary = models.IntegerField(null=True, blank=True)
    max_salary = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'jobs'
    def __str__(self):
        return self.job_title

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=25)
    phone_number = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField()
    job = models.ForeignKey('Job',on_delete=models.PROTECT)
    salary = models.IntegerField(null=True, blank=True)
    commission_pct = models.IntegerField(null=True, blank=True)
    manager = models.ForeignKey('self', null=True, blank=True,on_delete=models.PROTECT)
    department_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'employees'
    def __str__(self):
        return '%s %s %s %s ' % (self.first_name, self.last_name,self.job,
            self.salary)

class JobHistory(models.Model):
    employee = models.ForeignKey(Employee, primary_key=True,on_delete=models.PROTECT)
    start_date = models.DateField(unique=True)
    end_date = models.DateField()
    job = models.ForeignKey('Job',on_delete=models.PROTECT)
    department_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'job_history'
