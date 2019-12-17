
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from . import views

router = routers.DefaultRouter()

router.register('Employees', views.EmployeesView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('', include('employees.urls'))
]