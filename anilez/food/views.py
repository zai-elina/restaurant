from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


class FoodListView(ListView):
    model = Food
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class FoodPriceListView(ListView):
    model = Food
    template_name = 'menu_for_waiter.html'

    def get_context_data(self, **kwargs):
        context = super(FoodPriceListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def menuwaiter(request):
    return render(request, 'menu_for_waiter.html')

