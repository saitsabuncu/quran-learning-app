from django.urls import path
from .views import (
    memorized_surahs_view, memorize_page, unmemorize_page,
    RegisterView, CustomTokenObtainPairView, quran_surahs, 
    register_page, login_page, logout_page, UserProfileView, 
    AdminOnlyView, memorized_surahs_view, unmemorize_surah_view, 
    memorize_surah, get_memorized_surahs, unmemorize_surah, 
    get_memorized_pages
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('surahs/', quran_surahs, name="quran_surahs"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', CustomTokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', register_page, name="register_page"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('admin-panel/', AdminOnlyView.as_view(), name="admin_panel"),
    path('memorize/', memorize_surah, name="memorize_surah"),
    path('unmemorize/', unmemorize_surah, name="unmemorize_surah"),
    
    # Ezberlenen sureler ve sayfalar
    path("memorized-surahs/", memorized_surahs_view, name="memorized_surahs"),
    path("memorized-pages/", get_memorized_pages, name="get_memorized_pages"),
    
    # Ezberlenen sayfa ekleme ve silme
    path("memorize-page/", memorize_page, name="memorize_page"),
    path("unmemorize-page/<int:page_id>/", unmemorize_page, name="unmemorize_page"),
]
