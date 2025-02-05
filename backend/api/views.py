from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Surah

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def quran_surahs(request):
    surahs = Surah.objects.all().values("id", "number", "name", "verses")
    return JsonResponse(list(surahs), safe=False)

def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı otomatik giriş yaptır
            return redirect("login_page")  # Başarılı kayıt sonrası giriş sayfasına yönlendir
    else:
        form = UserCreationForm()
    return render(request, "api/register.html", {"form": form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home_page")  # Başarılı giriş sonrası ana sayfaya yönlendir
    else:
        form = AuthenticationForm()
    return render(request, "api/login.html", {"form": form})

def logout_page(request):
    logout(request)
    return redirect("login_page")  # Çıkış yaptıktan sonra login sayfasına yönlendir

