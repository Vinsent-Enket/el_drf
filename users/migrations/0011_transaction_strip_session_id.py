# Generated by Django 5.0.1 on 2024-03-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_transaction_status_alter_transaction_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='strip_session_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='идентификатор сессии'),
        ),
    ]