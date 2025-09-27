from django.contrib import admin
from django.utils.html import format_html
from .models import AudioSubmission, AudioAnalysisResult


@admin.register(AudioSubmission)
class AudioSubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "ayet", "notes", "uploaded_at")  # 👈 tabloda görünecek kolonlar
    search_fields = ("user__username", "ayet__text_ar", "notes")   # 👈 arama çubuğu
    list_filter = ("uploaded_at", "user")                          # 👈 sağ tarafta filtre

@admin.register(AudioAnalysisResult)
class AudioAnalysisResultAdmin(admin.ModelAdmin):
    list_display = ("id", "submission", "colored_similarity", "created_at")  # 👈 özel alanı ekledik
    
    search_fields = ("expected_text", "predicted_text")              # 👈 arama kutusu
    list_filter = ("created_at", "similarity")                       # 👈 filtreler    

    def colored_similarity(self, obj):
        if obj.similarity >= 80:
            color = "green"
        elif obj.similarity >= 50:
            color = "orange"
        else:
            color = "red"

        similarity_str = f"{obj.similarity:.2f}%"  # 👈 burada float'ı string'e çeviriyoruz
        return format_html('<span style="color: {};">{}</span>', color, similarity_str)

    colored_similarity.short_description = "Similarity"
