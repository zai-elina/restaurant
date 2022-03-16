from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


class FoodListView(ListView):
    model = Food
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

