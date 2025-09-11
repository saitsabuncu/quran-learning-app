from rest_framework import serializers
from .models import Surah, Ayet

class AyetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayet
        fields = ['id', 'number', 'text_ar', 'text_tr']

class SurahSerializer(serializers.ModelSerializer):
    ayets = AyetSerializer(many=True, read_only=True)  # `related_name='ayets'` üzerinden gelir

    class Meta:
        model = Surah
        fields = ['id', 'name', 'number', 'total_ayahs', 'ayets']
