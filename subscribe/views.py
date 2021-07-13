from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from subscribe.models import Subscribe
from subscribe.serializers import SubscribeSerializer
# Create your views here.


class SubscribeViewSet(viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    lookup_field = 'fans'

    @action(detail=True, methods=['get'])
    def info(self, request, username = None):
        queryset = Subscribe.objects.get(fans = username)
        serializer = SubscribeSerializer(queryset, many=False)
        return Response(serializer.data)