from django.shortcuts import render

# Create your views here.
from .serializers import EmployeesSerializer
from .models import Employees
from rest_framework import viewsets


class EmployeesView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
