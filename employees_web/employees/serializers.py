from rest_framework import serializers
from .models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employees_id', 'name', 'surname', 'email', 'phone_number', 'salary', 'job_id', 'department_id', 'thumb')