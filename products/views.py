from django.shortcuts import render,redirect

from .forms import ProductForm
from .models import Products


# Create your views here.

def getProducts(request):
    products = Products.objects.all()
    return render(request,'products/list.html',{'products' : products})

def createProducts(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_products') 
    form = ProductForm()
    return render(request,'products/create.html',{"form" : form})
