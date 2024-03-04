# Generated by Django 5.0.1 on 2024-03-04 21:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='user',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='proprietor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proprietor_of_sub', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.subscribe', verbose_name='Подписка'),
        ),
    ]
