from django.shortcuts import render, redirect
from django.views import View

from .models import Reviews
from .forms import ReviewForm


def about(request):
    return render(request, 'about.html')


def get_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
    else:
        # метод GET
        form = ReviewForm()
    # Получение всех имен из БД.
    reviews = Reviews.objects.all()
    # И добавляем names в контекст, чтобы получить к ним доступ в шаблоне
    return render(request, 'about.html', {'form': form, 'reviews': reviews})
