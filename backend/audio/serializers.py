from rest_framework import serializers
from .models import AudioSubmission
from .models import AudioAnalysisResult
from surahs.models import Ayet

class AyetMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayet
        fields = ['id', 'number', 'text_ar', 'text_tr']

class AudioSubmissionSerializer(serializers.ModelSerializer):
    ayet = AyetMiniSerializer(read_only=True)

    class Meta:
        model = AudioSubmission
        fields = ['id', 'ayet', 'audio_file', 'uploaded_at', 'is_checked', 'notes']

class AudioUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioSubmission
        fields = ['ayet', 'audio_file', 'notes']

class AudioAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioAnalysisResult
        fields = ["id", "submission", "expected_text", "predicted_text", "similarity", "created_at"]        
