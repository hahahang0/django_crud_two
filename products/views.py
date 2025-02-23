from django.shortcuts import render,redirect

from .forms import ProductForm
from .models import Products
from category.models import Category
from Branch.models import Branch



# Create your views here.

def getProducts(request):
    products = Products.objects.all()
    return render(request,'products/list.html',{'products' : products})

def createProducts(request):
    categories = Category.objects.all()
    branches = Branch.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_products') 
        else:
            print("Form errors:", form.errors) 
    form = ProductForm()
    return render(request,'products/create.html',{"form" : form,"categories":categories,'branches' : branches})
