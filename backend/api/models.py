from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

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

class MemorizedSurah(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Kullanıcı
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)  # Ezberlenen sure
    memorized_at = models.DateTimeField(auto_now_add=True)  # Ezberleme tarihi

    class Meta:
        unique_together = ("user", "surah")  # Aynı sureyi iki kez eklemeyi engelle

    def __str__(self):
        return f"{self.user.username} - {self.surah.name}"    

class MemorizedPage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    memorized_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'surah', 'page_number')

    def __str__(self):
        return f"{self.user.username} - {self.surah.name} - Sayfa {self.page_number}"

