from rest_framework import generics, permissions
from .models import TajweedRule
from .serializers import TajweedRuleSerializer

class TajweedRuleListView(generics.ListAPIView):
    queryset = TajweedRule.objects.all()
    serializer_class = TajweedRuleSerializer
    permission_classes = [permissions.AllowAny]
