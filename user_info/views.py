from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from user_info.serializers import UserRegisterSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'