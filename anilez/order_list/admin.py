from django.contrib import admin

from . import models

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date_order')

admin.site.register(models.Order,OrderAdmin)
admin.site.register(models.OrderItem)
