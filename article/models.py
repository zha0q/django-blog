from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import Markdown


class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%M%D')

class Article(models.Model):

    a_title = models.CharField(max_length=30)

    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )

    a_content = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        null = True,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    # category = models.ForeignKey(
    #     Category,
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='articles'
    # )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.a_title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.a_content)
        # toc 是渲染后的目录
        return md_body, md.toc

"""文章分类"""

#
# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     created = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         ordering = ['-created']
#
#     def __str__(self):
#         return self.title
