from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Официант")
    date_order=models.DateTimeField(auto_now=True,verbose_name="Дата заказа")
    complete=models.BooleanField(default=False,null=True,blank=False)
    table=models.IntegerField(default=0,verbose_name="Номер столика")
    total_price=models.DecimalField(default=0,max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.count for item in orderitems])
        return total

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-date_order']


class OrderItem(models.Model):
    food=models.ForeignKey('food.Food',on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    count=models.IntegerField(default=0,null=True,blank=True)
    date_add = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        total = self.food.price * self.count
        return total

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural="Элементы заказов"
