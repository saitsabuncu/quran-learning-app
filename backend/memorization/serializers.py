from rest_framework import serializers
from .models import MemorizedAyet
from surahs.models import Ayet

class AyetMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayet
        fields = ['id', 'number', 'text_ar', 'text_tr']

class MemorizedAyetSerializer(serializers.ModelSerializer):
    ayet = AyetMiniSerializer(read_only=True)

    class Meta:
        model = MemorizedAyet
        fields = ['id', 'ayet', 'date_memorized', 'note']
