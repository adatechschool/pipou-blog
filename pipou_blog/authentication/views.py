from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render

from . import forms


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = EmailAuthenticationForm


def register_page(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'authentication/register.html', context={'form': form})