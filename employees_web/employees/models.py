from django.db import models

class Employees(models.Model):
    employee_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    job_id = models.CharField(max_length=50)
    department_id = models.CharField(max_length=50)
    thumb = models.ImageField(default='default.png', blank=True)


    def __str__(self):
        return self.employee_id
