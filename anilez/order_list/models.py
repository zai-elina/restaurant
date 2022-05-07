from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    date_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    table=models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    food=models.ForeignKey('food.Food',on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    count=models.IntegerField(default=0,null=True,blank=True)
    date_add = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural="Элементы заказов"
