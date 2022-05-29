from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Reviews
from .forms import ReviewForm
# from .forms import ContactForm


def get_review(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({'name': name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = ReviewForm()
    # Получение всех имен из БД.
    reviews = Reviews.objects.all()
    return render(request, 'about.html', {'form': form, 'reviews': reviews})
