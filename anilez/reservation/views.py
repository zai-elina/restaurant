from django.http import JsonResponse
from django.shortcuts import render

from .models import Reservation
from .forms import ReservationTableForm

# from .forms import  ContactForm
def reserve_table(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ReservationTableForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({'name': name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = ReservationTableForm()
    # Получение всех имен из БД.
    # И добавляем names в контекст, чтобы получить к ним доступ в шаблоне
    return render(request, 'contact.html', {'form': form})

#
# def contact(request):
#     context={}
#     if request.method=='POST':
#         pass
#     else:
#         form=ContactForm()
#     context['form']=form
#     return render(request,'contact.html', context=context)
