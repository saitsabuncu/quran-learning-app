from django.contrib import admin
from django.utils.html import format_html, format_html_join
import json
from .models import AudioSubmission, AudioAnalysisResult


@admin.register(AudioSubmission)
class AudioSubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "ayet", "notes", "uploaded_at", "checked_status")
    search_fields = ("user__username", "ayet__text_ar", "notes")
    list_filter = ("uploaded_at", "user", "is_checked")

    def checked_status(self, obj):
        if obj.is_checked:
            return format_html('<span style="color: green;">✅ Checked</span>')
        return format_html('<span style="color: red;">❌ Not Checked</span>')

    checked_status.short_description = "Checked Status"


@admin.register(AudioAnalysisResult)
class AudioAnalysisResultAdmin(admin.ModelAdmin):
    list_display = ("id", "submission", "colored_similarity", "pretty_differences", "json_differences", "created_at")
    search_fields = ("expected_text", "predicted_text")
    list_filter = ("created_at", "similarity")
    readonly_fields = ("json_differences",)  # 👈 Detay sayfasında read-only alan olarak ekliyoruz

    def colored_similarity(self, obj):
        if obj.similarity >= 80:
            color = "green"
        elif obj.similarity >= 50:
            color = "orange"
        else:
            color = "red"
        similarity_str = f"{obj.similarity:.2f}%"
        return format_html('<span style="color: {};">{}</span>', color, similarity_str)
    colored_similarity.short_description = "Similarity"

    def pretty_differences(self, obj):
        if not obj.differences:
            return "-"
        try:
            diffs = obj.differences
            if isinstance(diffs, str):
                diffs = json.loads(diffs)
            return format_html_join(
                "<br>",
                '<span style="color:blue;">{}</span>: <span style="color:black;">{}</span>',
                ((d["type"], d.get("expected") or d.get("predicted")) for d in diffs)
            )
        except Exception:
            return str(obj.differences)
    pretty_differences.short_description = "Differences (Pretty)"

    def json_differences(self, obj):
        if not obj.differences:
            return "-"
        try:
            diffs = obj.differences
            if isinstance(diffs, str):
                diffs = json.loads(diffs)
            formatted = json.dumps(diffs, indent=2, ensure_ascii=False)
            return format_html(
                '<pre style="background-color:#f5f5f5; padding:10px; border-radius:5px; max-width:600px; white-space:pre-wrap;">{}</pre>',
                formatted
            )
        except Exception:
            return str(obj.differences)
    json_differences.short_description = "Differences (JSON)"
