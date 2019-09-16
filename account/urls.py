from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('login/', auth_view.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),

]