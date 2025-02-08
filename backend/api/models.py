from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True) # Kullanıcı girişini email ile yapacağız

    def __str__(self):
        return self.username
    
class Surah(models.Model):
    number = models.IntegerField(unique=True)  # Sure numarası (1, 2, 3...)
    name = models.CharField(max_length=255)  # Sure adı
    verses = models.IntegerField()  # Ayet sayısı
    arabic_text = models.TextField(blank=True, null=True)  # Arapça metin
    turkish_translation = models.TextField(blank=True, null=True)  # Türkçe meal
    pronunciation = models.TextField(blank=True, null=True)  # Okunuş

    def __str__(self):
        return f"{self.number} - {self.name}"    
