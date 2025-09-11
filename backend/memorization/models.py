from django.db import models
from django.contrib.auth import get_user_model
from surahs.models import Ayet

User = get_user_model()

class MemorizedAyet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorized_ayets')
    ayet = models.ForeignKey(Ayet, on_delete=models.CASCADE)
    date_memorized = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'ayet')  # Her kullanıcı bir ayeti sadece 1 kez ezberleyebilir

    def __str__(self):
        return f"{self.user.username} - {self.ayet}"
