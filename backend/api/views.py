from .models import MemorizedPage  # Eğer bu model varsa ekle
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import MemorizedSurah, Surah
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import MemorizedPage

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def quran_surahs(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Yetkisiz erişim!"}, status=403)
    surahs = Surah.objects.all().values("id", "number", "name", "verses", "arabic_text", "turkish_translation", "pronunciation")
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

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Kullanıcı giriş yapmadan erişemesin

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_staff:
            return Response({"error": "Yetkiniz yok!"}, status=403)

        return Response({"message": "Admin paneline hoş geldiniz!"})    


@api_view(["POST"])
@permission_classes([IsAuthenticated])  # Kullanıcı giriş yapmalı
def memorize_surah(request):
    user = request.user
    surah_id = request.data.get("surah_id")

    if not surah_id:
        return Response({"error": "Sure ID belirtilmelidir."}, status=400)

    surah = Surah.objects.filter(id=surah_id).first()
    if not surah:
        return Response({"error": "Sure bulunamadı."}, status=404)

    memorized, created = MemorizedSurah.objects.get_or_create(user=user, surah=surah)

    if created:
        return Response({"message": f"{surah.name} ezberlendi!"})
    else:
        return Response({"message": f"{surah.name} zaten ezberlenmiş."})

@api_view(["GET"])
@permission_classes([IsAuthenticated])  # Kullanıcı giriş yapmalı
def get_memorized_surahs(request):
    user = request.user
    memorized_surahs = MemorizedSurah.objects.filter(user=user).select_related("surah")
    data = [{"id": ms.surah.id, 
             "name": ms.surah.name, 
             "memorized_at": ms.memorized_at.strftime("%Y-%m-%d %H:%M:%S") # Tarihi okunabilir formatta gönder
             } 
             for ms in memorized_surahs
             ]
    return Response(data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])  # Kullanıcı giriş yapmalı
def unmemorize_surah(request):
    user = request.user
    surah_id = request.data.get("surah_id")

    if not surah_id:
        return Response({"error": "Sure ID belirtilmelidir."}, status=400)

    memorized = MemorizedSurah.objects.filter(user=user, surah_id=surah_id).first()
    
    if not memorized:
        return Response({"error": "Ezberlenmiş sure bulunamadı."}, status=404)

    memorized.delete()
    return Response({"message": "Sure ezberden kaldırıldı!"})

@login_required
def memorized_surahs_view(request):
    memorized_surahs = MemorizedSurah.objects.filter(user=request.user).select_related('surah')
    memorized_pages = MemorizedPage.objects.filter(user=request.user).select_related('surah')

    context = {
        'memorized_surahs': memorized_surahs,
        'memorized_pages': memorized_pages,
    }

    return render(request, 'api/memorized_surahs.html', context)

@csrf_exempt
@login_required
def unmemorize_surah_view(request, surah_id):
    if request.method == "POST":
        memorized = MemorizedSurah.objects.filter(user=request.user, surah_id=surah_id).first()
        if memorized:
            memorized.delete()
            return redirect("get_memorized_surahs")  # 🚀 Burada yönlendirme yapıyoruz
    return redirect("get_memorized_surahs")  # 🚀 Eğer sure bulunmazsa yine listeye yönlendirme

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def memorize_page(request):
    user = request.user
    surah_id = request.data.get('surah_id')
    page_number = request.data.get('page_number')

    if not surah_id or not page_number:
        return Response({'error': 'Sure ID ve sayfa numarası gereklidir.'}, status=400)

    surah = Surah.objects.filter(id=surah_id).first()
    if not surah:
        return Response({'error': 'Sure bulunamadı.'}, status=404)

    page, created = MemorizedPage.objects.get_or_create(user=user, surah=surah, page_number=page_number)

    if created:
        return Response({'message': f"{surah.name} suresinin {page_number}. sayfası ezberlendi!"})
    else:
        return Response({'message': f"{surah.name} suresinin {page_number}. sayfası zaten ezberlenmiş."})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_memorized_pages(request):
    user = request.user
    memorized_pages = MemorizedPage.objects.filter(user=user).select_related("surah")

    data = [
        {
            "surah_name": page.surah.name,
            "page_number": page.page_number,
            "memorized_at": page.memorized_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        for page in memorized_pages
    ]

    return Response(data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def unmemorize_page(request, page_id):
    user = request.user
    memorized_page = MemorizedPage.objects.filter(user=user, id=page_id).first()

    if not memorized_page:
        return Response({"error": "Ezberlenmiş sayfa bulunamadı."}, status=404)

    memorized_page.delete()
    return Response({"message": "Sayfa ezberden kaldırıldı!"})
