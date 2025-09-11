from rest_framework import generics
from .models import Surah, Ayet
from .serializers import SurahSerializer, AyetSerializer

class SurahListView(generics.ListAPIView):
    queryset = Surah.objects.all().order_by('number')
    serializer_class = SurahSerializer

class AyetListView(generics.ListAPIView):
    serializer_class = AyetSerializer

    def get_queryset(self):
        surah_id = self.request.query_params.get('surah')
        if surah_id:
            return Ayet.objects.filter(surah_id=surah_id).order_by('number')
        return Ayet.objects.none()
