from django.db import models
from .validators_files.fileValidators import file_size

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    category_image = models.FileField(upload_to="category_image/",null=True,blank=True,validators=[file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
