from django.urls import path
from .views import TajweedRuleListView

urlpatterns = [
    path('tajweed/', TajweedRuleListView.as_view(), name='tajweed-list'),
]
