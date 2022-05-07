from django.db.models import Q
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

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'menu_for_waiter.html')

class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'foods'

    def get_queryset(self):
        q=self.request.GET.get('s')
        return Food.objects.filter(Q(title__iregex=q))

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        return context