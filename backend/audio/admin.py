from django.contrib import admin
from .models import AudioSubmission, AudioAnalysisResult


@admin.register(AudioSubmission)
class AudioSubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "ayet", "notes", "uploaded_at")  # 👈 tabloda görünecek kolonlar
    search_fields = ("user__username", "ayet__text_ar", "notes")   # 👈 arama çubuğu
    list_filter = ("uploaded_at", "user")                          # 👈 sağ tarafta filtre

@admin.register(AudioAnalysisResult)
class AudioAnalysisResultAdmin(admin.ModelAdmin):
    list_display = ("id", "submission", "similarity", "created_at")  # 👈 tablo kolonları
    search_fields = ("expected_text", "predicted_text")              # 👈 arama kutusu
    list_filter = ("created_at", "similarity")                       # 👈 filtreler    