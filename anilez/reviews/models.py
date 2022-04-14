from django.db import models


class Reviews(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

