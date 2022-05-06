from django.urls import path
from . import views
from .views import Search

urlpatterns = [
    path('', views.home, name='index'),
    path('menu/', views.FoodListView.as_view(), name='menu'),
    path('menuwaiter/', views.FoodPriceListView.as_view(), name='menuwaiter'),
    path('search/', Search.as_view(), name='search'),
]