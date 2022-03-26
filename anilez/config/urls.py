from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
    path('news/', include('news.urls')),
]

# маршрут файлов media для отладочного режима
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documtnt_root=settings.MEDIA_ROOT)