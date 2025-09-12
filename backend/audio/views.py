from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import AudioSubmission
from .serializers import AudioSubmissionSerializer, AudioUploadSerializer

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
