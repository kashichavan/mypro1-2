from django.shortcuts import render,HttpResponse,redirect
from .forms import EmployeeForm,Employee
# Create your views here.

def home(request):
    return render(request,'home.html')

def insert(request):
    e=EmployeeForm()
    if request.method == 'POST':
        e1=EmployeeForm(request.POST)
        if e1.is_valid():
            e1.save()
            return redirect('myapp:viewdata')
        
    return render(request,'insert.html',{'form':e})

def viewdata(request):
    e=Employee.objects.all()
    return render(request,'view.html',{'emp':e})


def update(request,id):
    e=Employee.objects.get(id=id)
    if request.method == 'POST':
        e1=EmployeeForm(request.POST,instance=e)
        if e1.is_valid():
            e1.save()
            return redirect('myapp:viewdata')
    else:
        e1=EmployeeForm(instance=e)
        return render(request,'update.html',{'form':e1})

def delete(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('myapp:viewdata')

