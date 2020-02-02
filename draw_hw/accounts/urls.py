from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='reset'), 
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
