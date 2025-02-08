from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView
from .views import quran_surahs
from .views import register_page, login_page, logout_page
from .views import UserProfileView
from .views import AdminOnlyView

from .views import memorize_surah, get_memorized_surahs, unmemorize_surah

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
    path('memorized-surahs/', get_memorized_surahs, name="get_memorized_surahs"),
    path('unmemorize/', unmemorize_surah, name="unmemorize_surah"),
]
