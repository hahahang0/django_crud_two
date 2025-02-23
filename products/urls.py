from django.urls import path
from . import views

urlpatterns = [
    path("",views.getProducts, name='get_products'),
    path("create/",views.createProducts, name='create_products'),
    path("update/<int:pk>",views.updateProduct, name='update_product'),
    path("delete/<int:pk>",views.deleteProduct, name='delete_product'),
]