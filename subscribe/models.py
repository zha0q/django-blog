from django.db import models
from django.utils import timezone

from article.models import Article
from django.contrib.auth.models import User

# Create your models here.
class Subscribe(models.Model):

    fans = models.TextField()

    blogger = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.blogger