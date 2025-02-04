from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True) # Kullanıcı girişini email ile yapacağız

    def __str__(self):
        return self.username
