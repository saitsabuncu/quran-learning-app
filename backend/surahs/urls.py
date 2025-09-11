from django.urls import path
from .views import SurahListView, AyetListView

urlpatterns = [
    path('surahs/', SurahListView.as_view(), name='surah-list'),
    path('ayets/', AyetListView.as_view(), name='ayet-list'),
]
