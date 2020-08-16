from django.db import models

class Article(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    check = models.BooleanField(default = False)

    def __str__(self):
        return self.name

