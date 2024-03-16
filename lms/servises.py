from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms.models import Course
from lms.tasks import mail_sender
from users.models import Subscribe, User


def notifier(course):
    print(course)
    users_emails = []
    subs = course.courses_sub.all()
    for sub in subs:
        users_emails.append(sub.proprietor.email)
    mail_sender.delay(header='Сообщение от платформы', message=f'Пользователь, был обновлен курс {course.name}',
                      recipient_list=users_emails)

