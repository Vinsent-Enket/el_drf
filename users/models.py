from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Subscribe(models.Model):
    """
    Можете меня побить за то что я отошел от ТЗ. Но мне кажется логичнее создать один объект подписки, привязать его к пользователю
    и уже в нем убавлять/добавлять подписки, просто создавать его не отдельным эндпоинтом, а при создании юзера
    """
    proprietor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                   related_name='proprietor_of_sub',
                                   verbose_name='Владелец')
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс на которые подписан', **NULLABLE)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Личная почта')
    subscribe = models.ForeignKey(Subscribe, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Подписка')
    # name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    # last_name = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
    # email_verification_token = models.CharField(max_length=255, verbose_name='Токен для регистрации', **NULLABLE)
    # email_is_verify = models.BooleanField(default=False, verbose_name='Емейл верифицирован')
    # phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    # avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    # user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
    #                                           related_name='user_set',
    #                                           related_query_name='user', to='auth.permission',
    #                                           verbose_name='user permissions')
    # is_blocked = models.BooleanField(default=False, verbose_name='Заблокирован')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Transaction(models.Model):
    payment_method_choice = [('ch', 'Pay to cash'),
                             ('cd', 'Pay to card'), ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь совершивший транзакцию')
    date = models.DateField(auto_now=True, verbose_name='Время транзакции')
    purchased_course = models.ManyToManyField(Course, verbose_name='Купленные курсы', blank=True)
    purchased_lessons = models.ManyToManyField(Lesson, verbose_name='Купленные отдельные уроки', blank=True)
    payment_amount = models.PositiveIntegerField(
        verbose_name='Сумма оплаты', default=0)  # добавить ли тогда каждому уроку цену? И как тогда будет считаться цена за курс? Просто по сумме стоимости уроков в него входящих + скидка или фиксированный прайс?
    payment_method = models.CharField(choices=payment_method_choice, max_length=50, verbose_name='Способ оплаты')
    status = models.BooleanField(default=False, verbose_name='Статус оплаты')
    strip_session_id = models.CharField(max_length=50, **NULLABLE, verbose_name='идентификатор сессии')

    def __str__(self):
        return f'{self.user}, {self.date}, {self.payment_amount}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
