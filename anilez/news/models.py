from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    photo = models.ImageField(upload_to='photo/%Y/%m', blank=True, verbose_name="Изображение")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']