from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_confirmation_email(email, confirmation_code):
    subject = "Your Login Confirmation Code"
    message = f"Your confirmation code is: {confirmation_code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
