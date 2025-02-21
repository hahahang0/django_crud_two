from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import BranchForm


# Create your views here.
from .models import Branch

def get_branch(request):
    branch = Branch.objects.all()
    return render(request,'branch/branch_list.html',{'branches' : branch})


def create_branch(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
        
    form = BranchForm()
    return render(request,'branch/create.html',{'form' : form})


def update_branch(request,pk):
    branch = get_object_or_404(Branch,id = pk)
    if request.method == "POST":
        form = BranchForm(request.POST,instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    form = BranchForm(instance=branch)
    return render(request,'branch/update.html',{'form': form})

def delete_branch(request,pk):
    branch = get_object_or_404(Branch,id=pk)
    if request.method == "POST": 
        branch.delete()
    return redirect('branch_list')


