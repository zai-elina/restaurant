from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django import forms
from django.contrib.auth import login, logout
from .forms import RegistrForm

def register(request):
    if request.method == "POST":
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = RegistrForm()
    return render(request, 'register.html', {"form": form})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-conrol'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-conrol'}))


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('waiter')
    else:
        form = UserLoginForm()
    return render(request, 'login.html',  {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')

def waiter(request):
    return render(request, 'waiter.html')

