from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email')
    phone = PhoneNumberField(blank=True, null=True, verbose_name='Телефон', help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars/', null=True, verbose_name='Аватар', help_text='Добавьте изображение')
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name='Страна', help_text='Укажите страну')
    token = models.CharField(max_length=100, verbose_name='Токен', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
