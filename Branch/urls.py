from django.urls import path
from . import views
urlpatterns = [

    path('',views.get_branch,name="branch_list"),
    path('create/',views.create_branch,name="create_branch"),
    path('update/<int:pk>',views.update_branch,name="update_branch"),
    path('delete/<int:pk>',views.delete_branch,name="delete_branch"),
]