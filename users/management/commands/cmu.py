import random
import time

from django.contrib.auth.models import Group, Permission
from users.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Надо ли и тут прятать логины пароли в переменные окружения????"""

    def handle(self, *args, **options):
        now = int(time.time())
        manager_group = Group.objects.create(name='Менеджер') # а как удалять не в ручную?
        # Получение прав на просмотр всех категорий и моделей без возможности изменения
        view_permissions = Permission.objects.filter(codename__startswith='view_')




        # Для начала следует обратиться к типу контента для нужной модели
        content_type = ContentType.objects.get_for_model(User)
        # получить запись о необходимых правах доступа
        set_blocked_permissions = Permission.objects.get(
            codename="set_blocked",
            content_type=content_type,
        )

        manager_group.permissions.set(view_permissions)
        manager_group.permissions.add(set_blocked_permissions)

        username = f'employee{now}'
        password = str(random.shuffle(list(username)))
        email = f'{username}@example.com'
        with open("manager_data.txt", "a") as file:
            file.write(f' email-{email}\n'
                       f' password-{password}\n\n')
        user = User.objects.create(
            self_email=email,
            first_name='Tot',
            last_name='Unhamon',

        )
        user.set_password(password)
        user.groups.add(manager_group)
        user.save()
