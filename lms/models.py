from django.db import models

from config import settings

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lesson/', verbose_name='Превью', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE, default=None)
    proprietor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                   verbose_name='Владелец')
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='course/', **NULLABLE)
    lessons = models.ManyToManyField(Lesson, verbose_name='Уроки курса')
    proprietor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                   verbose_name='Владелец')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    stripe_product_id = models.CharField(max_length=50, verbose_name='Айди курса на Stripe', default='')
    stripe_price_id = models.CharField(max_length=50, verbose_name='Айди цены на Stripe', default='')


    @property
    def latest_update(self):
        last_lesson = self.lessons.order_by('-created_at').first()
        return last_lesson.created_at

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
