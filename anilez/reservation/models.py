from django.core.validators import RegexValidator
from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя посетителя")
    email = models.EmailField()
    phone = models.CharField(max_length=16, validators=[RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?["
                                                                             r"\d\- ]{7,10}$")], verbose_name="Номер телефона")
    number_of_person = models.IntegerField(verbose_name="Количество")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    is_reserved = models.BooleanField(default=False, verbose_name="Забронировано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Бронирование"


