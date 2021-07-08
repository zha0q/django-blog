from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
