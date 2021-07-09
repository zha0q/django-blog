
from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView

urlpatterns = [
    path(r'api/', include('article.urls')),
    path('admin/', admin.site.urls),
    path(r'^', TemplateView.as_view(template_name='index.html')),
]
