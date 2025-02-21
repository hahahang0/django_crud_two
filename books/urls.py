from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.getBooks,name="books_list"),
    path('create/',views.createBooks,name="createBooks"),
    path('update/<int:pk>',views.updateBooks,name="updateBooks"),
    path('delete/<int:pk>',views.deleteBooks,name="deleteBooks"),

]