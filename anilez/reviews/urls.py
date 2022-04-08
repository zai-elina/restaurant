from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path("review/", views.get_review, name="review"),
]