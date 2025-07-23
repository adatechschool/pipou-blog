from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from . import forms

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'],)
            if user is not None:
                print("user is not None")
                login(request, user)
                message = f'Bonjour, {user.first_name} Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'

    return render(request, 'authentication/login.html', context={'form': form, 'message': message})
  

def logout_user(request):
    logout(request)
    return redirect('login')