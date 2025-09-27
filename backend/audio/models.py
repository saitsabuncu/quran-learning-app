from django.db import models
from django.db.models import JSONField
from django.contrib.auth import get_user_model
from surahs.models import Ayet

User = get_user_model()

class AudioSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_submissions')
    ayet = models.ForeignKey(Ayet, on_delete=models.CASCADE, related_name='audio_submissions')
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        # Kullanıcı + Sure adı + Ayet numarası + Submission id
        return f"{self.user.username} - {self.ayet.surah.name} {self.ayet.number} (#{self.id})"


class AudioAnalysisResult(models.Model):
    submission = models.ForeignKey("AudioSubmission", on_delete=models.CASCADE, related_name="analyses")
    expected_text = models.TextField()
    predicted_text = models.TextField()
    similarity = models.FloatField()
    differences = models.JSONField(default=list, blank=True)  # 👈 yeni alan
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Analiz id + submission id + benzerlik yüzdesi
        return f"Analysis {self.id} for Submission {self.submission.id} - {self.similarity:.2f}%"
