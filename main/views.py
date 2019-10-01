from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import permission_required,login_required
from .forms import *



def index(request):
    employee = Employee.objects.all()
    return render(request, 'main/index.html', {'employee': employee})


@permission_required('is_superuser', raise_exception=True)
def home(request):
    leave = Leave.objects.all().filter(status= 'pending...')
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
        'present': present,
        'absent': absent,
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
def employee(request):
    employee = Employee.objects.all().order_by('-id')
    return render(request, 'main/employees.html', {'employee': employee})


@login_required(login_url='login')
def employ(request, name):
    user = request.user
    employee = Employee.objects.all().filter(name=name).filter(name=user)
    total = 12
    count = Leave.objects.all().filter(user=request.user).filter(status='Granted').count()
    available = total - count
    content = {
        'employee': employee,
        'total': total,
        'count': count,
        'available': available,
        }

    return render(request, 'main/employ.html', content)


def leave(request):
    form = LeaveForm(request.POST or None)

    if form.is_valid():
        leave = form.save(commit=False)
        leave.user = request.user
        if leave.date < datetime.now().date():
            leave.status = "Granted"
        leave.save()
        return redirect('/')

    return render(request, 'main/leave.html')


def entry(request):
    form = EntryForm(request.POST or None)

    if form.is_valid():
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        return redirect('/')
    return render(request, 'main/entry.html')


def exit(request):
    form = ExitForm(request.POST or None)
    if form.is_valid():
        exit = form.save(commit=False)
        exit.user = request.user
        now = datetime.now()
        time = now.strftime("%H")
        if time < '4':
            exit.status = "Half Day"
        else:
            exit.status = "Full Day"
        exit.save()
        return redirect('/')
    else:
        return render(request, 'main/exit.html')


def attendance(request, user):
    entry = Entry.objects.filter(user=request.user)
    exit = Exit.objects.filter(user=request.user)
    now = datetime.now()
    month = now.strftime("%B")
    context = {
        'exit': exit,
        'entry':entry,
        'month': month,
    }
    return render(request, "main/details.html", context)


def grant(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == 'POST':
        leave.status = "Granted"
        leave.save()
        return redirect('/home')

    return render(request, 'main/grant.html', {'leave': leave})


def reject(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if request.method == 'POST':
        leave.status = "rejected"
        leave.save()
        return redirect('/home')

    return render(request, 'main/reject.html', {'leave': leave})


@login_required
def profile(request):
    return HttpResponseRedirect(reverse('detail', args=[request.user.username]))


def all_attendence(request):
    entry = Entry.objects.all()
    exit = Exit.objects.all()
    context = {
        'entry': entry,
        'exit': exit,
    }
    return render(request, 'main/attendance.html', context)


def all_leave(request):
    leave = Leave.objects.all()
    return render(request, 'main/leaves.html', {'leave': leave})


def leaves(request, user):
    leave = Leave.objects.filter(user=request.user)
    context = {
        'leave':leave,
    }
    return render(request, "main/leaves.html", context)



