
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('create/', views.create, name='create'),
    path('employee/edit/<int:pk>/', views.edit, name='edit'),
    path('employee/<int:pk>/', views.employ, name='detail'),
    path('employee/delete/<int:pk>/', views.delete, name='delete'),
    path('employee/', views.employee, name='employee'),
    path('leave/', views.leave, name='leave'),
]