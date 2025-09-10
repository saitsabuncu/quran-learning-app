from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    progress = models.JSONField(default=dict, blank=True)  # ezber ilerleme, vb.

    def __str__(self):
        return self.username
