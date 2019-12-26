from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from .serializers import EmployeesSerializer
from .models import Employees
from rest_framework import viewsets


class EmployeesView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_default_renderer(self, view):
        return JSONRenderer()


def index(request):
    employees = Employees.objects.all().order_by('employees_id')
    return render(request, 'index.html', {'Employees': employees})


def employees_list(request, slug):
    employees = Employees.objects.get(slug=slug)
    return render(request, 'employees_list.html', {'Employees': employees})
