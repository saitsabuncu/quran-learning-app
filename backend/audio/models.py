from django.db import models
from django.contrib.auth import get_user_model
from surahs.models import Ayet
from django.conf import settings

User = get_user_model()

class AudioSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_submissions')
    ayet = models.ForeignKey(Ayet, on_delete=models.CASCADE, related_name='audio_submissions')
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - Ayet {self.ayet.number} - {self.uploaded_at.strftime('%Y-%m-%d')}"

class AudioAnalysisResult(models.Model):
    submission = models.ForeignKey("AudioSubmission", on_delete=models.CASCADE, related_name="analyses")
    expected_text = models.TextField()
    predicted_text = models.TextField()
    similarity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.submission} - {self.similarity}%"