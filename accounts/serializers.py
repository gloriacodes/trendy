# accounts/serializers.py
from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import User

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password')
