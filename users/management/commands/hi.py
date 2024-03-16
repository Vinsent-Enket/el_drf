from django.core.management import BaseCommand
from celery import shared_task
import django
from django.utils import timezone
from datetime import timedelta, datetime

from users.models import User
from users.models import Subscribe


class Command(BaseCommand):

    def handle(self, *args, **options):
        now = timezone.now().strftime("%Y-%m-%d")
        print(now)
        print(now[:4], now[5:7], now[8:])
        now_converted = datetime(year=int(now[:4]), month=int(now[5:7]), day=int(now[8:]))
        print(now_converted)
        month = timedelta(days=30)
        users = User.objects.all()

        for user in users:
            if user.last_login == None:
                continue
            user_last_login = user.last_login.strftime("%Y-%m-%d")
            user_last_login_converted = datetime(year=int(user_last_login[:4]), month=int(user_last_login[5:7]),
                                                 day=int(user_last_login[8:]))
            if now_converted - month > user_last_login_converted:
                print(f'этого юзера - {user.email}  банить')
            else:
                print(f'а этот юзер - {user.email}  норм')


