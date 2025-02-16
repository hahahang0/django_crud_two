from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=200)
    employee_email = models.EmailField(unique=True)
    employee_contact = models.CharField(max_length = 20,unique=True,null=True,blank=True)
    employee_address = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.employee_name
