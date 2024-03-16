from celery import shared_task
from django.utils import timezone
from datetime import timedelta, datetime

from users.models import User


@shared_task
def users_check_login():
    now = timezone.now().strftime("%Y-%m-%d")
    print(now)
    print(now[:4], now[5:7], now[8:])
    now_converted = datetime(year=int(now[:4]), month=int(now[5:7]), day=int(now[8:]))
    print(now_converted)
    month = timedelta(days=30)
    users = User.objects.all()

    for user in users:
        if user.last_login is None:
            continue
        user_last_login = user.last_login.strftime("%Y-%m-%d")
        user_last_login_converted = datetime(year=int(user_last_login[:4]), month=int(user_last_login[5:7]),
                                             day=int(user_last_login[8:]))
        if now_converted - month > user_last_login_converted:
            user.is_active = False
            print(f'этого юзера - {user.email}  банить')
        else:
            print(f'а этот юзер - {user.email}  норм')
