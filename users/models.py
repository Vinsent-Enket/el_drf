from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    description = models.TextField(verbose_name='Описание')
    proprietor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                   verbose_name='Владелец', related_name='Director')



class User(AbstractUser):
    username = None
    self_email = models.EmailField(unique=True, verbose_name='Личная почта')
    work_email = models.EmailField(verbose_name='Рабочая почта', **NULLABLE)
    name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
    # company = models.ForeignKey
    email_verification_token = models.CharField(max_length=255, verbose_name='Токен для регистрации', **NULLABLE)
    email_is_verify = models.BooleanField(default=False, verbose_name='Емейл верифицирован')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                              related_name='user_set',
                                              related_query_name='user', to='auth.permission',
                                              verbose_name='user permissions')
    is_blocked = models.BooleanField(default=False, verbose_name='Заблокирован')
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.SET_NULL, **NULLABLE)
    # appointment = models.CharField(max_length=50, choices=)
    USERNAME_FIELD = "self_email"
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'set_blocked',
                'can_blocked_user'
            )
        ]


# class Director(AbstractUser):
#     username = None
#     self_email = models.EmailField(unique=True, verbose_name='Личная почта')
#     work_email = models.EmailField(verbose_name='Рабочая почта', **NULLABLE)
#     name = models.CharField(max_length=30, verbose_name='Имя пользователя')
#     last_name = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
#     # company = models.ForeignKey
#     email_verification_token = models.CharField(max_length=255, verbose_name='Токен для регистрации', **NULLABLE)
#     email_is_verify = models.BooleanField(default=False, verbose_name='Емейл верифицирован')
#     phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
#     avatar = models.ImageField(upload_to='director/', verbose_name='Аватар', **NULLABLE)
#     user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this director.',
#                                               related_name='director_set',
#                                               related_query_name='director', to='auth.permission',
#                                               verbose_name='director permissions')
#     USERNAME_FIELD = "self_email"
#     REQUIRED_FIELDS = []

