from django.urls import path
from .views import (
    AudioSubmissionListView,
    AudioSubmissionUploadView,
    AudioFeedbackView,
)
from .views import AudioAnalyzeView

urlpatterns = [
    path('audio/', AudioSubmissionListView.as_view(), name='audio-list'),
    path('audio/upload/', AudioSubmissionUploadView.as_view(), name='audio-upload'),
    path('audio/feedback/<int:pk>/', AudioFeedbackView.as_view(), name='audio-feedback'),
    path('audio/analyze/<int:pk>/', AudioAnalyzeView.as_view(), name='audio-analyze'),
]
