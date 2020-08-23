from django.db import models
from users.models import User
# import sys
# sys.path.append('../')
# from users.models import *

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=100, 
        error_messages={
            'unique': ("This article already exists.")
            },
    )
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10)
    user = models.ForeignKey('users.User', verbose_name='ユーザー名', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'user'], name='unique_booking'),
        ]

    def __str__(self):
        return self.title

