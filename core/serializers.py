from rest_framework import serializers
from .models import Core


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = "__all__"
