from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def quran_surahs(request):
    surahs = [
        {"id": 1, "name": "Al-Fatiha", "verses": 7},
        {"id": 2, "name": "Al-Baqarah", "verses": 286},
        {"id": 3, "name": "Al-Imran", "verses": 200},
    ]
    return JsonResponse(surahs, safe=False)

