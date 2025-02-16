from django.urls import path,include 
from . import views
urlpatterns = [
    path('',views.getEmployees,name="list"),
    path('create/',views.createEmployee,name="createEmp")
]