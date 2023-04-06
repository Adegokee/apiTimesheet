from django.urls import path
from . import views



urlpatterns = [
    path('', views.add_employee, name='add_employee'),
    path('modify_employee/<int:employee_id>/', views.modify_employee, name='modify_employee'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('generate_payslip/', views.generate_payslip, name='generate_payslip'),
    path('start_break/', views.start_break, name='start_break'),
    path('end_break/', views.end_break, name='end_break'),
     path('clock_out/', views.clock_in, name='clock_out'),
      path('clock_in/', views.clock_in, name='clock_in'),
     
     
     
   
]
