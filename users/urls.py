from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLogoutView, UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('users/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout/', CustomLogoutView.as_view(), name='logout'),
    path('users/register', UserCreateView.as_view(), name='register'),
    path('users/email-confirm/<str:token>/', email_verification, name='email-confirm'),
]
