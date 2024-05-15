from time import sleep

from django import forms
from django.core.mail import send_mail


class FeedbackForm(forms.Form):
    email = forms.EmailField(label='Your email')
    message = forms.CharField(
        label="Feedback Form", widget=forms.Textarea(attrs={"rows": 5, "cols": 20})
    )

    def send_email(self):
        """
        Sends an email when the feedback form has been submitted
        :return:
        """
        subject = "Your Feedback"
        message = f"Your feedback has been received:\n\n{self.cleaned_data['message']}"
        from_email = self.cleaned_data["email"]
        to_email = "support@example.com"
        sleep(10)  # Simulate a slow email server
        send_mail(subject, message, from_email, [to_email])
        print("Email sent")
