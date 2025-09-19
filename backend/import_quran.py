import json
import os
import django

# Django ayarlarını yükle
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from surahs.models import Surah, Ayet

with open("backend/data/quran-uthmani.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Tanzil JSON formatı: data → surahs → ayahs
for surah in data["data"]["surahs"]:
    surah_id = surah["number"]          # Sure numarası
    for ayah in surah["ayahs"]:
        number = ayah["numberInSurah"]  # Ayetin sure içindeki numarası
        text_ar = ayah["text"]          # Ayetin Arapça metni

        # Senin admin panelinde girdiğin Surah kaydı ile eşleştiriyoruz
        surah_obj = Surah.objects.get(id=surah_id)

        Ayet.objects.get_or_create(
            surah=surah_obj,
            number=number,
            defaults={"text_ar": text_ar}
        )

print("✅ Ayetler başarıyla import edildi.")