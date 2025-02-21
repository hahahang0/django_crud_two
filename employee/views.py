# from django.shortcuts import render
from .models import Employee
from django.shortcuts import redirect,render,get_object_or_404
from .forms import EmployeeForm

# Create your views here.
def getEmployees(request):
    employees = Employee.objects.all()
    return render(request,'employee/list.html',{'employees':employees})

def createEmployee(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        
    else: 
        form = EmployeeForm()
    return render(request,'employee/create.html',{'form':form})

def updateEmployee(request,pk):
    employee = get_object_or_404(Employee,employee_id=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES,instance=employee)
        if request.method == "POST":
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request,'employee/update.html',{'form':form})

# def deleteEmployee(request,pk):
#     employee = get_object_or_404(Employee,employee_id=pk)
#     if request.method == "POST":
#         employee.delete()
#     return redirect('list')


def deleteEmployee(request,pk): 
    # employee = Employee.objects.get(id=pk)
    employee = get_object_or_404(Employee,employee_id=pk)
    if request.method == "POST":
        employee.delete()
    return redirect('list')

def globalView(request):
    return render(request,'employee/global.html')
