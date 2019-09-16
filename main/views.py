from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect,reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import permission_required,login_required
from .forms import *



def index(request):
    employee = Employee.objects.all()
    return render(request, 'main/index.html', {'employee': employee})


@permission_required('is_superuser', raise_exception=True)
def home(request):
    leave = Leave.objects.all()
    entry = Entry.objects.all().filter(start_time__date__day=datetime.now().day)
    exit = Exit.objects.all().filter(end_time__date__day=datetime.now().day)
    count = Employee.objects.all().count()
    present = entry.count()
    absent = count - present

    context = {
        'leave': leave,
        'entry': entry,
        'exit': exit,
        'count': count,
        'present':present,
        'absent':absent,
    }
    return render(request, 'main/home.html', context)


@permission_required('is_superuser', login_url='login')
def create(request):
    form = EmployeeForm(request.POST or None, request.FILES)

    if form.is_valid():
        if User.DoesNotExist:
            user = User.objects.create_user(request.POST['name'], password=request.POST['password'])
            form.save()
            auth.login(request, user)
            return redirect('/')

    return render(request, 'main/create.html')


@permission_required('is_superuser', raise_exception=True)
def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('/')

    context = {'employee': employee}
    return render(request, 'main/delete.html', context)


@permission_required('is_superuser', raise_exception=True)
def edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'main/edit.html', {'employee': employee})


@permission_required('is_superuser', raise_exception=True)
def employee(request):
    employee = Employee.objects.all()
    return render(request, 'main/employees.html', {'employee': employee})

@login_required
def employ(request, name):
    employee = Employee.objects.all().filter(name=name)
    return render(request, 'main/employ.html', {'employee': employee})


def leave(request):
    form = LeaveForm(request.POST or None)

    if form.is_valid():
        leave = form.save(commit=False)
        leave.user = request.user
        leave.save()
        messages.success(request, 'your leave request has been sent.')
        return redirect('/')
    return render(request, 'main/leave.html')


def entry(request):
    form = EntryForm(request.POST or None)

    if form.is_valid():
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        messages.success(request, 'your attendance has been saved.')
        return redirect('/')
    return render(request, 'main/entry.html')


def exit(request):
    form = ExitForm(request.POST or None)

    if form.is_valid():
        exit = form.save(commit=False)
        exit.user = request.user
        exit.save()
        messages.success(request, 'your attendance has been saved.')
        return redirect('/')
    return render(request, 'main/exit.html')


def attendance(request, user):
    entry = Entry.objects.filter(user=request.user)
    exit = Exit.objects.filter(user=request.user)
    context = {
        'exit': exit,
        'entry':entry,
    }
    return render(request, "main/details.html", context)


def grant(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == 'POST':
        leave.status = "Granted"
        leave.save()
        messages.success(request, 'leave granted')
        return redirect('/home')

    return render(request, 'main/grant.html', {'leave': leave})


def reject(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == 'POST':
        leave.status = "rejected"
        leave.save()
        messages.success(request, 'leave rejected')
        return redirect('/home')

    return render(request, 'main/reject.html', {'leave': leave})


@login_required
def profile(request):
    return HttpResponseRedirect(reverse('detail', args=[request.user.username]))



