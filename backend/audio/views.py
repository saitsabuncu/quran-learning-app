from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import AudioSubmission
from rest_framework.exceptions import PermissionDenied
from .serializers import AudioSubmissionSerializer, AudioUploadSerializer
from .analyze import analyze_audio_submission

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

    def post(self, request, pk):
        try:
            submission = AudioSubmission.objects.get(pk=pk, user=request.user)
        except AudioSubmission.DoesNotExist:
            return Response({"detail": "Kayıt bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        
        # Ayet metni ve ses dosyası yolu
        ayet_text = submission.ayet.text_ar
        audio_path = submission.audio_file.path

        # Whisper analizi
        result = analyze_audio_submission(audio_path, ayet_text)

        return Response(result, status=status.HTTP_200_OK)           
