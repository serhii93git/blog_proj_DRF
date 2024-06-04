from django.db import models

from django.contrib.auth.models import AbstractUser


class Creator(AbstractUser):
    """A model for posts author"""

    creator_image = models.ImageField(upload_to='creator_img/', blank=True, null=True)

    def __str__(self):
        return self.username
