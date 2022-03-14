from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('about/', views.about, name='about'),
    path('menu/', views.FoodListView.as_view(), name='menu'),

]