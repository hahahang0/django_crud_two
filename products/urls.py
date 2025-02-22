from django.urls import path
from . import views

urlpatterns = [
    path("",views.getProducts, name='get_products'),
    path("create/",views.createProducts, name='create_products'),
]