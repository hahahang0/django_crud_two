from django.shortcuts import render,redirect,get_object_or_404

from .forms import ProductForm
from .models import Products
from category.models import Category
from Branch.models import Branch
from django.http import HttpResponse



# Create your views here.

def getProducts(request):

    # products = Products.objects.all()
    products = Products.objects.select_related("product_category", "branch").all()
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
            # Form is invalid, re-render the page with error messages and the old values
            return render(request,'products/create.html',{"form" : form,"categories":categories,'branches' : branches})
    form = ProductForm()
    return render(request,'products/create.html',{"form" : form,"categories":categories,'branches' : branches})


def updateProduct(request,pk):
    categories = Category.objects.all()
    branches = Branch.objects.all()
    products  = get_object_or_404(Products,product_id = pk)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=products)
        if form.is_valid():
            form.save()
            return redirect('get_products') 
        else:
            # Form is invalid, re-render the page with error messages and the old values
            return render(request,'products/create.html',{"form" : form,"categories":categories,'branches' : branches})
    form = ProductForm(instance=products)
    return render(request,'products/create.html',{"form" : form,"categories":categories,'branches' : branches})

def deleteProduct(request,pk):
    products = get_object_or_404(Products,product_id = pk)
    if request.method == "POST":
        products.delete()
        return  redirect('get_products')