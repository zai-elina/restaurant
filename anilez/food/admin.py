from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Food)