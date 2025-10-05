from django.db import models
from django.db.models import JSONField
from django.contrib.auth import get_user_model
from surahs.models import Ayet

User = get_user_model()

# 1️⃣ Kullanıcı bazlı dosya yolu oluşturma fonksiyonu
def user_audio_path(instance, filename):
    # Örn: audio/user_5/2_255_recitation.mp3
    return f"audio/user_{instance.user.id}/{instance.ayet.surah.number}_{instance.ayet.number}_{filename}"

class AudioSubmission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Beklemede'),
        ('checking', 'İnceleniyor'),
        ('approved', 'Onaylandı'),
        ('rejected', 'Reddedildi'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_submissions')
    ayet = models.ForeignKey(Ayet, on_delete=models.CASCADE, related_name='audio_submissions')
    audio_file = models.FileField(upload_to=user_audio_path)  # 🔁 Artık kullanıcı bazlı klasörlere yüklenir
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # ✅ Yeni eklendi
    notes = models.TextField(blank=True)

    def __str__(self):
        # Kullanıcı + Sure adı + Ayet numarası + Submission id
        return f"{self.user.username} - {self.ayet.surah.name} {self.ayet.number} (#{self.id})"
    
    


class AudioAnalysisResult(models.Model):
    submission = models.ForeignKey("AudioSubmission", on_delete=models.CASCADE, related_name="analyses")
    expected_text = models.TextField()
    predicted_text = models.TextField()
    similarity = models.FloatField(help_text="0–100 arası benzerlik yüzdesi")  # ✅ Açıklama eklendi
    differences = models.JSONField(default=list, blank=True, null=True)  # ✅ null=True eklendi
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Analiz id + submission id + benzerlik yüzdesi
        return f"Analysis {self.id} for Submission {self.submission.id} - {self.similarity:.2f}%"
