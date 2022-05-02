from django import forms

from .models import Reservation


class ReservationTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


# class ContactForm(forms.Form):
#     name=forms.CharField(min_length=2,
#                          widget=forms.TextInput(
#                              attrs={'placeholder':'Ваше имя'}))
#     email = forms.EmailField(widget=forms.EmailInput(
#                              attrs={'placeholder':'Ваша почта'}))
#     message=forms.CharField(min_length=20,
#                            widget=forms.Textarea(
#                                attrs={'placeholder':'Сообщение','cols':30,'rows': 9}))