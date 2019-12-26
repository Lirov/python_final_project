from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from . import views

router = routers.DefaultRouter()

router.register('Employees', views.EmployeesView)
app_name = 'employees'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('index/', views.index, name="index"),
    path('<slug:slug>/', views.employees_list, name="employees_list"),

]
