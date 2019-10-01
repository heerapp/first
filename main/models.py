from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save

STAFF_CHOICES = [
    ('Web Developer', 'developer'),
    ('Receptionist', 'receptionist'),
    ('Manager', 'manager'),
    ('Designer', 'designer'),
]


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=STAFF_CHOICES)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/")


def create_employee(sender, **kwargs):
    if kwargs['created']:
        Employee.objects.create(user=kwargs['instance'])


post_save.connect(create_employee, sender=User)


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user


class Exit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    end_time = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=50, default="Full Day")

    def __str__(self):
        return f"{self.user}"


class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=50, default="pending...", blank=True)

    def __str__(self):
        return f"{self.user}"






