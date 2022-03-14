from django.shortcuts import render
# from django.views.generic import ListView

# from anilez.food.models import Food


def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')



