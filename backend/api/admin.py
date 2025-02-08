from django.contrib import admin
from .models import Surah

@admin.register(Surah)
class SurahAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "verses")  # Admin panelinde hangi sütunlar gözüksün
    search_fields = ("name", "number")  # Arama yaparken kullanılacak alanlar
    

