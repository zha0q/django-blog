
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView


urlpatterns = [
    path('api/', include('article.urls')),
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
