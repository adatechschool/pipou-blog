from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm

from . import forms


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = EmailAuthenticationForm
