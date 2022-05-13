from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.cart, name='order'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('waiter/', views.waiter, name='waiter'),
    path(r'^status/(?P<id>\d+)/$', views.status, name='status'),
]