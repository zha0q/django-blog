from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from user_info.serializers import UserRegisterSerializer, UserDescSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'

    @action(detail=True, methods=['get'])
    def info(self, request, username = None):
        queryset = User.objects.get(username = username)
        serializer = UserDescSerializer(queryset, many=False)
        return Response(serializer.data)