from rest_framework import serializers
from .models import Employee, Timesheet, Payroll

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ('id', 'user', 'is_admin')

# class TimesheetSerializer(serializers.ModelSerializer):
#     employee = serializers.ReadOnlyField(source='employee.user.username')

#     class Meta:
#         model = TimeSheet
#         fields = ('id', 'employee', 'clock_in', 'clock_out', 'break_start', 'break_end')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'
