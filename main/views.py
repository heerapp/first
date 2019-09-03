from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import permission_required
from .forms import EmployeeForm

def home(request):
    employee = Employee.objects.all()
    attendance = Attendance.objects.all()
    leave = Leave.objects.all()
    context={
        'employee' : employee,
        'attendance' : attendance,
        'leave' : leave
        }
    return render(request,'main/home.html',context)

@permission_required('is_superuser')
def create(request):
    form = EmployeeForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        if User.DoesNotExist:
            user = User.objects.create_user(request.POST['name'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('/employee')

    return render(request,'main/create.html')

@permission_required('is_superuser')
def delete(request,pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('/')

    context = {'employee':employee}
    return render(request,'main/delete.html', context)

@permission_required('is_superuser')
def edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'main/edit.html',{'employee':employee})

def employee(request):
    employee = Employee.objects.all()
    return render(request, 'main/employees.html',{'employee':employee})


def employ(request, pk):
    employee = Employee.objects.all().filter(pk=pk)
    return render(request, 'main/employ.html',{'employee':employee})

