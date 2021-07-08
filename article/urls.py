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
router.register('article', ArticleViewSet)
router.register('comment', CommentViewSet)
router.register('user', UserViewSet)

# router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]