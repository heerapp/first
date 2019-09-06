from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name


class Attendance(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Leave(models.Model):
    date = models.DateField()
    reason = models.TextField()
