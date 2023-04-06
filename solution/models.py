

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(null=True, blank=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    break_start = models.DateTimeField(null=True, blank=True)
    break_end = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __unicode__(self):
        return self.employee

