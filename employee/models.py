from django.db import models
from .validators_files.fileValidators import file_size


# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=200)
    employee_email = models.EmailField(unique=True)
    employee_contact = models.CharField(max_length = 20,unique=True,null=True,blank=True)
    employee_address = models.CharField(max_length=200,null=True,blank=True)
    employee_image = models.FileField(upload_to='employee_profile_image/',null=True,blank=True,validators=[file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_name
