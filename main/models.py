from django.db import models
from datetime import datetime

class Employee(models.Model):
    name = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.employee

class Leave(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    days = models.IntegerField(default=1)
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return self.employee
