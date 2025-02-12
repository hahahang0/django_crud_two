from django.shortcuts import render
from .models import Employee
from django.shortcuts import redirect,render,get_object_or_404
from .forms import EmployeeForm

# Create your views here.
def getEmployees(request):
    employees = Employee.objects.all()
    return render(request,'list.html',{'employees':employees})

def createEmployee(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        
    else: 
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})

def updateEmployee(request,pk):
    employee = get_object_or_404(Employee,employee_id=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if request.method == "POST":
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request,'update.html',{'form':form})

def deleteEmployee(request,pk):
    employee = get_object_or_404(Employee,employee_id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('list')
