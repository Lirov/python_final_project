from django.shortcuts import render

from rest_framework import viewsets
from .models import Employees
from . serializers import employeesSerializer

class EmployeesView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = employeesSerializer
