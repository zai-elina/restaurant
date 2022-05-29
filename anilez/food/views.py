from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def home(request):
    return render(request, 'index.html')


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


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'foods'

    def get_queryset(self):
        q=self.request.GET.get('s')
        return Food.objects.filter(Q(title__iregex=q))

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        return context