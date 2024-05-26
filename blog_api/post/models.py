from django.db import models


class Post(models.Model):
    """Model for blog posts"""

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='files/', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    author = models.CharField(max_length=50)  # to do: connect to User model

    def __str__(self):
        return self.title
