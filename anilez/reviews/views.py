from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Reviews
from .forms import ReviewForm
from .forms import ContactForm


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
    # И добавляем names в контекст, чтобы получить к ним доступ в шаблоне
    return render(request, 'about.html', {'form': form, 'reviews': reviews})


def contact(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'],
                         form.cleaned_data['email'],
                         form.cleaned_data['message'],
                         form.cleaned_data['phone'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context=context)


def send_message(name, email, message, phone):
    pass
