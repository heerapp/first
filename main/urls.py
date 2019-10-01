
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('employ/acer/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('employee/<slug:name>/', views.employ, name='detail'),
    path('employee/', views.employee, name='employee'),
    path('leave/', views.leave, name='leave'),
    path('entry/', views.entry, name='entry'),
    path('exit/', views.exit, name='exit'),
    path('details/<slug:user>/', views.attendance, name='attendance'),
    path('grant/<int:pk>/', views.grant, name='grant'),
    path('reject/<int:pk>/', views.reject, name='reject'),
    path('profile/', views.profile, name='profile'),
    path('attendance/', views.all_attendence, name='attendances'),
    path('leaves/', views.all_leave, name='leaves'),
    path('employee/<slug:user>/leaves/', views.leaves, name='user-leaves'),
    path('employ/<slug:name>/', views.profiles, name='employs'),
]