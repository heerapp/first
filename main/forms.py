from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['address', 'contact', 'type', 'image']


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ('user',)


class ExitForm(forms.ModelForm):
    class Meta:
        model = Exit
        exclude = ('user', 'status',)


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        exclude = ('user',)



