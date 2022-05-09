from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *
from django.apps import apps
Food = apps.get_model('food', 'Food')

def cart(request):
    if request.user.is_authenticated:
        customer=request.user
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}
    context={'items':items,'order':order}
    return render(request, 'order.html', context)

def updateItem(request):
    data = json.loads(request.body)
    foodId = data['foodId']
    action =data['action']
    print('Action:',action)
    print('foodId:', foodId)

    customer=request.user
    food=Food.objects.get(id=foodId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem,created=OrderItem.objects.get_or_create(order=order,food=food)

    if action=='add':
        orderItem.count=(orderItem.count+1)
    elif action=='remove':
        orderItem.count = (orderItem.count - 1)


    orderItem.save()

    if orderItem.count <=0:
        orderItem.delete()
    return JsonResponse('Food was added', safe=False)

def processOrder(request):
    data = json.loads(request.body)
    print("DATA:",request.body)
    if request.user.is_authenticated:
        customer=request.user
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        total=data['form']['total']
        total=total.replace(',','.')
        total=float(total)
        if total==order.get_cart_total:
            order.complete=True
            order.total_price=total
            order.table=data['form']['table']
        order.save()
    else:
        print('User is not logged in')

    return JsonResponse('Order was added', safe=False)

def waiter(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(complete=True)
    else:
        order={'get_cart_total':0, 'get_cart_items':0}
    context={'order':order}
    return render(request, 'waiter.html', context)

