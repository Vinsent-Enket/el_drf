from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='lesson/', verbose_name='Превью', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)


class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='course/', **NULLABLE)
    lessons = models.ManyToManyField(Lesson, verbose_name='Уроки курса', **NULLABLE)

