from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ('user',)


class ExitForm(forms.ModelForm):
    class Meta:
        model = Exit
        exclude = ('user',)


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        exclude = ('user',)




