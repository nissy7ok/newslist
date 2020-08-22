from django.db import models
# import sys
# sys.path.append('../')
# from users.models import *

class Article(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(
        max_length=100, 
        unique=True, 
        error_messages={
            'unique': ("This article already exists.")
            },
    )
    url = models.URLField(max_length=200, unique=True)
    name = models.CharField(max_length=100, unique=True)
    # user = models.ForeignKey('User', verbose_name='ユーザー名', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

