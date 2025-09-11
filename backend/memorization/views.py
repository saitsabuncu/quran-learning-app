from rest_framework import generics, permissions
from .models import MemorizedAyet
from .serializers import MemorizedAyetSerializer
from surahs.models import Ayet
from rest_framework.response import Response
from rest_framework import status

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
