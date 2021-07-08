from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment.views import CommentViewSet
from user_info.views import UserViewSet
from article.views import ArticleViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)

# router.register('category', views.CategoryViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]