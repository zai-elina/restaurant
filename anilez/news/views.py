from django.shortcuts import render

from .models import News


def news(request):
    model = News.objects.all()
    context = {'news': model}
    return render(request, 'news.html', context=context)
