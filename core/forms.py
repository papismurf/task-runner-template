from time import sleep

from django import forms

from core.tasks import send_feedback_email_task


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
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
