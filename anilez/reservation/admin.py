from django.contrib import admin

from . import models


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'is_reserved')
    search_fields = ('name', 'date', 'time')


admin.site.register(models.Reservation, ReservationAdmin)
