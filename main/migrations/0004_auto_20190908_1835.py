# Generated by Django 2.2.4 on 2019-09-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190908_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exit',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
