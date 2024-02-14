import os

from django.core.mail import send_mail
from django.core.management import BaseCommand

from config import settings
from users.models import User


class Command(BaseCommand):
    """Надо ли и тут прятать логины пароли в переменные окружения????"""
    def handle(self, *args, **options):
        print(os.getenv('YANDEX_LOGIN'))
        print(os.getenv('YANDEX_PASSWORD'))

        send_mail(
            subject='Вы сменили пароль',
            message=f'Ваш новый пароль:',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=('bersercer100@gmail.com',)
        )
        print('hu')
