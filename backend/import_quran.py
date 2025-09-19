import json
import os
import django

# Django ayarlarını yükle
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from surahs.models import Surah, Ayet

with open("backend/quran.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    surah_id = item["surah"]
    number = item["ayah"]
    text_ar = item["text_ar"]

    surah = Surah.objects.get(id=surah_id)  # senin admin panelden eklediğin sure kaydı
    Ayet.objects.get_or_create(
        surah=surah,
        number=number,
        defaults={"text_ar": text_ar}
    )

print("✅ Ayetler başarıyla import edildi.")
