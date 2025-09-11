from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import AudioSubmission
from .serializers import AudioSubmissionSerializer, AudioUploadSerializer

class AudioSubmissionListView(generics.ListAPIView):
    serializer_class = AudioSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AudioSubmission.objects.filter(user=self.request.user).order_by('-uploaded_at')


class AudioSubmissionUploadView(generics.CreateAPIView):
    serializer_class = AudioUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
