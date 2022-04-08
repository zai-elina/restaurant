from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('menu/', views.FoodListView.as_view(), name='menu'),
]