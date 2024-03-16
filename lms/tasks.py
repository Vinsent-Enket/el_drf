from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def mail_sender(header, message, recipient_list):
    try:
        send_mail(
            subject=header,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list
        )
    except Exception:
        print('Ну не шмогла')
    else:
        print('отправилось сообщение')

