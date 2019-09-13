from django.shortcuts import render,redirect
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.user.is_staff:
                return redirect('home/')
            else:
                pk = str(request.user.pk-1)
                return redirect('employee/'+ pk)
        else:
            return render(request, 'account/login.html', {'error': 'username or password is incorrect.'})

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
