from django.contrib import admin

from .models import Employee, Timesheet, Payroll

# Register your models here.
admin.site.register(Employee)
admin.site.register(Timesheet)
admin.site.register(Payroll)
