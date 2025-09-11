from django.urls import path
from .views import ListCreateMemorizedAyet, DeleteMemorizedAyet

urlpatterns = [
    path('memorized/', ListCreateMemorizedAyet.as_view(), name='memorized-list-create'),
    path('memorized/<int:ayet_id>/', DeleteMemorizedAyet.as_view(), name='memorized-delete'),
]
