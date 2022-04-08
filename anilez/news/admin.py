from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    search_fields = ('title', 'content')


admin.site.register(models.News, NewsAdmin)
