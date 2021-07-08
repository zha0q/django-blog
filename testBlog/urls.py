
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from article.views import IndexTemplateView

urlpatterns = [
    path(r'api/', include('article.urls')),
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name="entry-point")
]
