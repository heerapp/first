from django import forms
from .models import Employee,Attendance,Leave


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class StartAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["start_time"]

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ["date","reason"]
