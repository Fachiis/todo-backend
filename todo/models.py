from django.db import models
from django.conf import settings
from datetime import datetime


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Todo(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    reminder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=False, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
