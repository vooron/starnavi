from django.urls import path

from .views import RegistrationView

urlpatterns = [
    path(r'registration', RegistrationView.as_view()),
]
