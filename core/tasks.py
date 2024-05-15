from time import sleep

from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_feedback_email_task(email, message):
    """
    Sends an email when the feedback form has been submitted
    :return:
    """
    subject = "Your Feedback"
    message = f"Your feedback has been received:\n\n{message}"
    from_email = email
    to_email = "contact@example.com"
    sleep(10) # Simulate a long-running task
    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False
    )
