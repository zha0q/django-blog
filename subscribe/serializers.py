# -*- codeing = utf-8 -*-
# @Time : 2021/7/13 18:21
# @File : serializers.py
# @Software : PyCharm
from subscribe.models import Subscribe
from rest_framework import serializers


class SubscribeSerializer(serializers.ModelSerializer):
    """于文章列表中引用的嵌套序列化器"""
    class Meta:
        model = Subscribe
        fields = '__all__'