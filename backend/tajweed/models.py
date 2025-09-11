from django.db import models

class TajweedRule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example_ar = models.TextField(help_text="Ayet örneği - Arapça")
    example_tr = models.TextField(help_text="Ayet anlamı - Türkçe", blank=True)
    audio_url = models.URLField(blank=True, help_text="Opsiyonel: Sesli örnek")

    def __str__(self):
        return self.name
