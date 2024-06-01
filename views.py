from django.shortcuts import render,redirect
from .forms import employeeForm
from .models import employee
def home(request):
    obj=employee.objects.all()
    return render(request,'home.html',{'data':obj})
def create(request):
    if request.method=='POST':
        myform=employeeForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect("read")
        return redirect("create")
    else:
        myform=employeeForm
        return render(request,'create.html',{'form':myform})
def update(request,id):
    obj=employee.objects.get(id=id)
    if request.method=='POST':
        myform=employeeForm(request.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('read')
        return redirect('create')
    else:
        myform=employeeForm
        return render(request,'update.html',{'form':myform})
def delete(request,id):
    obj = employee.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('read')
    return render(request,'delete.html')

# Create your views here.
