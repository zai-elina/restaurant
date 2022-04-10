from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_review, name="about"),
    path('contact/', views.contact, name='contact'),
]