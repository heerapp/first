# Generated by Django 2.2.4 on 2019-09-08 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_employee_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
