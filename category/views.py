from django.shortcuts import render,redirect,get_object_or_404
from .models import Category
from .forms import CategoryForm


# Create your views here.

def getCategory(request):
    categories = Category.objects.all()
    return render(request,'category/list.html',{'categories':categories})

def createCategory(request):
    if request.method == "POST" : 
       form = CategoryForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('category_list')
    form = CategoryForm()
    return render(request,'category/create.html',{'form' : form})

def updateCategory(request,pk):
    category = get_object_or_404(Category,category_id = pk)
    if request.method == "POST" : 
        form = CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    form = CategoryForm(instance=category)
    return render(request,'category/update.html',{'form' : form})


def deleteCategory(request,pk):
    category = get_object_or_404(Category,category_id = pk)
    if request.method == "POST":
        category.delete()
    return redirect('category_list')