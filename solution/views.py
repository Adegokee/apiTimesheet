from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import EmployeeSerializer, TimesheetSerializer, PayrollSerializer

from .models import Employee, Timesheet, Payroll




@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def modify_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'success': False, 'message': 'Employee not found'}, status=404)

    serializer = EmployeeSerializer(employee, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def clock_in(request):
    serializer = TimesheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def clock_out(request, timesheet_id):
    try:
        timesheet = Timesheet.objects.get(id=timesheet_id)
    except Timesheet.DoesNotExist:
        return Response({'success': False, 'message': 'Timesheet not found'}, status=404)

    timesheet.clock_out = request.data.get('clock_out')
    timesheet.save()

    serializer = TimesheetSerializer(timesheet)
    return Response(serializer.data)


@api_view(['POST'])
def start_break(request, timesheet_id):
    try:
        timesheet = Timesheet.objects.get(id=timesheet_id)
    except Timesheet.DoesNotExist:
        return Response({'success': False, 'message': 'Timesheet not found'}, status=404)

    timesheet.break_start = request.data.get('break_start')
    timesheet.save()

    serializer = TimesheetSerializer(timesheet)
    return Response(serializer.data)


@api_view(['POST'])
def end_break(request, timesheet_id):
    try:
        timesheet = Timesheet.objects.get(id=timesheet_id)
    except Timesheet.DoesNotExist:
        return Response({'success': False, 'message': 'Timesheet not found'}, status=404)

    timesheet.break_end = request.data.get('break_end')
    timesheet.save()

    serializer = TimesheetSerializer(timesheet)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_payslip(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'success': False, 'message': 'Employee not found'}, status=404)

    payroll = Payroll.objects.filter(employee=employee)
    if not payroll:
        return Response({'success': False, 'message': 'Payroll not found'}, status=404)

    serializer = PayrollSerializer(payroll, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def generate_report(request):
#     payroll = Payroll.objects.all()
#     report_data = {}

#     for p in payroll:
#         employee = p.employee.name
#         amount = p.amount

#         if employee not in report_data:
#             report_data[employee] =

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_report(request):
    payroll = Payroll.objects.all()
    report_data = {}

    for p in payroll:
        employee = p.employee.name
        amount = p.amount

        if employee not in report_data:
            report_data[employee] = amount
        else:
            report_data[employee] += amount

    return Response(report_data)