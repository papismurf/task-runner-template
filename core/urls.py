from django.contrib import admin
from django.urls import path

from core.views import FeedbackFormView, SuccessView

app_name = "core"

urlpatterns = [
    path("", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
]
