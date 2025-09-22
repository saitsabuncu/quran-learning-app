from rest_framework import generics, permissions
from .models import MemorizedAyet
from .serializers import MemorizedAyetSerializer
from surahs.models import Ayet, Surah
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ListCreateMemorizedAyet(generics.ListCreateAPIView):
    serializer_class = MemorizedAyetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MemorizedAyet.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        ayet_id = request.data.get('ayet_id')
        note = request.data.get('note', '')

        try:
            ayet = Ayet.objects.get(id=ayet_id)
        except Ayet.DoesNotExist:
            return Response({'error': 'Ayet bulunamadı'}, status=status.HTTP_404_NOT_FOUND)

        memorized, created = MemorizedAyet.objects.get_or_create(
            user=request.user,
            ayet=ayet,
            defaults={'note': note}
        )

        if not created:
            return Response({'error': 'Bu ayet zaten ezberlenmiş'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(memorized)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeleteMemorizedAyet(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        ayet_id = kwargs.get('ayet_id')
        try:
            memorized = MemorizedAyet.objects.get(user=request.user, ayet_id=ayet_id)
            memorized.delete()
            return Response({'message': 'Silindi'}, status=status.HTTP_204_NO_CONTENT)
        except MemorizedAyet.DoesNotExist:
            return Response({'error': 'Ezber kaydı bulunamadı'}, status=status.HTTP_404_NOT_FOUND)

class MemorizationStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        total_ayets = Ayet.objects.count()
        memorized_ayets = MemorizedAyet.objects.filter(user=user).count()

        # Avoid division by zero
        overall_percentage = (memorized_ayets / total_ayets * 100) if total_ayets > 0 else 0
        surah_stats = []
        
        #Sıralama eklendi
        surahs = Surah.objects.all().order_by("id")

        for surah in surahs:
            surah_total = Ayet.objects.filter(surah=surah).count()
            surah_memorized = MemorizedAyet.objects.filter(user=user, ayet__surah=surah).count()
            percentage = (surah_memorized / surah_total * 100) if surah_total > 0 else 0

            surah_stats.append({
                "surah_id": surah.id,
                "surah_name": surah.name,
                "memorized": surah_memorized,
                "total": surah_total,
                "percentage": round(percentage, 2)
            })

        return Response({
            "total_memorized": memorized_ayets,
            "total_ayets": total_ayets,
            "overall_percentage": round(overall_percentage, 2),
            "by_surah": surah_stats
        })    