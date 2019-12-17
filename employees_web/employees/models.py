from django.db import models


# Create your models here.
class Employees(models.Model):

    employees_id = models.CharField(max_length=50)
    # name = models.CharField(max_length=50)
    # surname = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    # phone_number = models.CharField(max_length=50)
    # salary = models.CharField(max_length=50)
    # job_id = models.CharField(max_length=50)
    # department_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title

