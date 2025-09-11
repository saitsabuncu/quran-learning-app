from rest_framework import serializers
from .models import TajweedRule

class TajweedRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TajweedRule
        fields = '__all__'
