from django.urls import path,include 
from . import views
urlpatterns = [
    path('employee/',views.getEmployees,name="list"),
    path('create/',views.createEmployee,name="createEmp"),
    path('update/<int:pk>',views.updateEmployee,name="editEmp"),
    path('delete/<int:pk>',views.deleteEmployee,name="deleteEmp"),
    path('',views.globalView,name="globalView"),

]