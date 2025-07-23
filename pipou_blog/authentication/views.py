from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm

from . import forms


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = EmailAuthenticationForm



""" def logout_user(request):
    logout(request)
    return redirect('login') """