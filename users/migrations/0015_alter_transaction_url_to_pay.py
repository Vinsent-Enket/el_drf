# Generated by Django 5.0.1 on 2024-03-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_transaction_url_to_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='url_to_pay',
            field=models.TextField(default='', verbose_name='Ссылка на оплату'),
        ),
    ]