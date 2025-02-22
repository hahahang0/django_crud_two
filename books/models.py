from django.db import models
from .validators_files.fileValidators import file_size

# Create your models here.

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=50)
    book_description = models.CharField(max_length=200,null=True,blank=True)
    book_author = models.CharField(max_length=100,null=True,blank=True)
    book_page = models.IntegerField(null=True,blank=True)
    book_publications = models.CharField(max_length=200,null=True,blank=True)
    book_image = models.FileField(upload_to="books/",null=True,blank=True,validators=[file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.book_title
