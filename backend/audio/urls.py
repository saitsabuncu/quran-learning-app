from django.urls import path
from .views import AudioSubmissionListView, AudioSubmissionUploadView

urlpatterns = [
    path('audio/', AudioSubmissionListView.as_view(), name='audio-list'),
    path('audio/upload/', AudioSubmissionUploadView.as_view(), name='audio-upload'),
]
