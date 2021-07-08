from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from article.models import Article
from article.serializers import ArticlesSerializer, ArticlesDetailSerializer
from rest_framework.permissions import IsAuthenticated

from django.views.generic.base import TemplateView

#
# class CategoryViewSet(viewsets.ModelViewSet):
#     """分类视图集"""
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticlesSerializer
        else:
            return ArticlesDetailSerializer

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = AritclesSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
