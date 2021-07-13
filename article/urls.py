from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment.views import CommentViewSet
from user_info.views import UserViewSet
from article.views import ArticleViewSet, AvatarViewSet
from subscribe.views import SubscribeViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)
router.register(r'avatar', AvatarViewSet)
router.register(r'subscribe', SubscribeViewSet)

# router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]