from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")

    # def clean_email(self):
    #     email = self.cleaned_data['email'].strip()
    #     if Reviews.objects.filter(email=email).exists():
    #         raise ValidationError("Пользователь с данной почтой уже оставлял комментaрий")
    #     return email


