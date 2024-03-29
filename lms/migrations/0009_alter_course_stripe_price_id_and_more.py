# Generated by Django 5.0.1 on 2024-03-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_course_price_course_stripe_price_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='stripe_price_id',
            field=models.CharField(default='', max_length=50, verbose_name='Айди цены на Stripe'),
        ),
        migrations.AlterField(
            model_name='course',
            name='stripe_product_id',
            field=models.CharField(default='', max_length=50, verbose_name='Айди курса на Stripe'),
        ),
    ]
