from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )  # чтобы сделать подкатегории

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Food(models.Model):
    img = models.ImageField(upload_to='menu', blank=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name="food",
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='price')

    def __str__(self):
        return self.title
