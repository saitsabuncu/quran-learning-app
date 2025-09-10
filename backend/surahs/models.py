from django.db import models

class Surah(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(unique=True)
    total_ayahs = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.number}. {self.name}"

class Ayet(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE, related_name='ayets')
    number = models.PositiveIntegerField()
    text_ar = models.TextField()
    text_tr = models.TextField(blank=True)

    def __str__(self):
        return f"{self.surah.name} - {self.number}"