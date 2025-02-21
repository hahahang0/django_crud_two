from django.urls import path
from .  import views 
urlpatterns = [
    path('',views.getCategory,name="category_list"),
    path('create/',views.createCategory,name="create_category"),
    path('update/<int:pk>',views.updateCategory,name="update_category"),
    path('delete/<int:pk>',views.deleteCategory,name="delete_category"),

]