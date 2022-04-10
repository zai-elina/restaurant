from django import forms
from django.core.validators import RegexValidator

from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Почта'}
    ))
    message = forms.CharField(max_length=300, widget=forms.Textarea(
        attrs={'placeholder': 'Напишите дату и время', 'cols': 21,
               'rows': 2}))
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone = forms.CharField(validators=[phoneNumberRegex], max_length=16, widget=forms.TextInput(
        attrs={'placeholder': 'Номер телефона'}))
