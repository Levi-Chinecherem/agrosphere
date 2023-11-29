# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
    path('newsfeed/', include('newsfeed.urls')),
    path('sharing/', include('sharing.urls')),
]

# Optionally, serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
