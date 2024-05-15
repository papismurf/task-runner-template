from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import FormView

from core.forms import FeedbackForm


class FeedbackFormView(FormView):
    template_name = 'core/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('core:success')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'core/success.html'
