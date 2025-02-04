from django.urls import path
from .views import quran_surahs

urlpatterns = [
    path('surahs/', quran_surahs, name="quran_surahs"),
]
