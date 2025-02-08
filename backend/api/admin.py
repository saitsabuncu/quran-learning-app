from django.contrib import admin
from .models import Surah, MemorizedSurah

@admin.register(Surah)
class SurahAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "verses")  # Admin panelinde hangi sütunlar gözüksün
    search_fields = ("name", "number")  # Arama yaparken kullanılacak alanlar
    
@admin.register(MemorizedSurah)
class MemorizedSurahAdmin(admin.ModelAdmin):
    list_display = ("user", "surah", "memorized_at")  # Admin panelinde gösterilecek alanlar
    search_fields = ("user__username", "surah__name")  # Kullanıcı ve sure adına göre arama
