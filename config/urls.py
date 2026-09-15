from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), path('accounts/', include('accounts.urls')),
    path('gate/', include('gate.urls')), path('patrol/', include('patrol.urls')),
    path('incidents/', include('incidents.urls')), path('shifts/', include('shifts.urls')),
    path('', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
