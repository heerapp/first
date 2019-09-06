from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth.decorators import permission_required
from .forms import EmployeeForm, StartAttendanceForm, LeaveForm

def index(request):
    return render(request,'main/index.html')

@permission_required('is_superuser',raise_exception=True)
def home(request):
    employee = Employee.objects.all()
    attendance = Attendance.objects.all()
    leave = Leave.objects.all()
    context = {
        'employee': employee,
        'attendance': attendance,
        'leave': leave
    }
    return render(request, 'main/home.html', context)


@permission_required('is_superuser',login_url='login')
def create(request):
    form = EmployeeForm(request.POST or None, request.FILES)

    if form.is_valid():
        if User.DoesNotExist:
            user = User.objects.create_user(request.POST['name'], password=request.POST['password'])
            form.save()
            auth.login(request, user)
            return redirect('/employee')

    return render(request, 'main/create.html')


@permission_required('is_superuser',raise_exception=True)
def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('/')

    context = {'employee': employee}
    return render(request, 'main/delete.html', context)


@permission_required('is_superuser',raise_exception=True)
def edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'main/edit.html', {'employee': employee})

@permission_required('is_superuser',raise_exception=True)
def employee(request):
    employee = Employee.objects.all()
    return render(request, 'main/employees.html', {'employee': employee})


def employ(request, pk):
    employee = Employee.objects.all().filter(pk=pk)
    form = StartAttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/home')
    return render(request, 'main/employ.html', {'employee': employee})


def leave(request):
    form = LeaveForm(request.POST or None)
    pk = str(request.user.pk - 1)

    if form.is_valid():
        form.save()
        messages.success(request,'your leave request has been sent.')
        return redirect('/employee/'+pk)
    return render(request, 'main/leave.html')
