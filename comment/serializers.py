# -*- codeing = utf-8 -*-
# @Time : 2021/7/6 12:07
# @File : serializers.py
# @Software : PyCharm
from django.contrib.auth.models import User
from rest_framework import serializers
from user_info.serializers import UserDescSerializer
from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}



