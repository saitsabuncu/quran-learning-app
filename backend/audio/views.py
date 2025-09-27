import whisper
from difflib import SequenceMatcher
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import AudioSubmission, AudioAnalysisResult
from rest_framework.exceptions import PermissionDenied
from .serializers import AudioSubmissionSerializer, AudioUploadSerializer
from .serializers import AudioAnalysisResultSerializer
from .analyze import analyze_audio_submission

# Load Whisper model once (not every request)
model = whisper.load_model("base")

def analyze_audio_submission(audio_path, expected_text):
    result = model.transcribe(audio_path, language="ar")
    predicted_text = result['text'].strip()
    similarity = SequenceMatcher(None, expected_text, predicted_text).ratio()

    return {
        "expected": expected_text,
        "predicted": predicted_text,
        "similarity": round(similarity * 100, 2)
    }

# Kullanıcının kendi kayıtlarını listeleme
class AudioSubmissionListView(generics.ListAPIView):
    serializer_class = AudioSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AudioSubmission.objects.filter(user=self.request.user).order_by('-uploaded_at')

# Kullanıcının yeni kayıt yüklemesi
class AudioSubmissionUploadView(generics.CreateAPIView):
    serializer_class = AudioUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Admin'in geri bildirim (not ve kontrol) işlemi
class AudioFeedbackView(generics.UpdateAPIView):
    queryset = AudioSubmission.objects.all()
    serializer_class = AudioSubmissionSerializer
    permission_classes = [permissions.IsAdminUser]  # sadece admin

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Sadece admin kullanıcılar düzenleyebilir.")
        return super().update(request, *args, **kwargs) 


class AudioAnalyzeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):  # 👈 format parametresi eklendi
        try:
            submission = AudioSubmission.objects.get(pk=pk, user=request.user)
        except AudioSubmission.DoesNotExist:
            return Response({"error": "Audio submission not found"}, status=status.HTTP_404_NOT_FOUND)

        ayet = submission.ayet
        audio_path = submission.audio_file.path
        expected_text = ayet.text_ar

        # Analizi yap
        result = analyze_audio_submission(audio_path, expected_text)

        # DB'ye kaydet
        analysis = AudioAnalysisResult.objects.create(
            submission=submission,
            expected_text=result["expected"],
            predicted_text=result["predicted"],
            similarity=result["similarity"],
        )

        serializer = AudioAnalysisResultSerializer(analysis)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


