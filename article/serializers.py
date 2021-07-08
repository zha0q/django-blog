from rest_framework import serializers

from article.models import Article
from user_info.serializers import UserDescSerializer
from comment.serializers import CommentSerializer

# class CategorySerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='category-detail')
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         read_only_fields = ['created']


class ArticlesBaseSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    id = serializers.IntegerField(read_only=True)


    url = serializers.HyperlinkedIdentityField(view_name="article-detail")



class ArticlesSerializer(ArticlesBaseSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}

class ArticlesDetailSerializer(ArticlesBaseSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    # 渲染后的正文
    body_html = serializers.SerializerMethodField()
    # 渲染后的目录
    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'


        # fields = [
        #     'id',
        #     'a_title',
        #     'created',
        #     'author',
        #     'url',
        # ]

        # category = CategorySerializer(read_only=True)
        #
        # category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
        #
        # def validate_category_id(self, value):
        #     if not Category.objects.filter(id=value).exists() and value is not None:
        #         raise serializers.ValidationError("Category with id {} not exists.".format(value))
        #     return value

        # 新增字段，添加超链接