# Generated by Django 2.2.4 on 2019-10-01 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(choices=[('Web Developer', 'developer'), ('Receptionist', 'receptionist'), ('Manager', 'manager'), ('Designer', 'designer')], max_length=100)),
                ('email', models.CharField(default='abc@gmail.com', max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(blank=True, default='pending...', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Full Day', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
