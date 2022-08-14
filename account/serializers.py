from rest_framework import serializers
from .models import SeggleUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeggleUser
        fields = ['id', 'username', 'email', 'name', 'is_staff', 'is_superuser', 'joined_date', 'is_active']

class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = SeggleUser
        fields = ['username', 'name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeggleUser
        fields = ['id', 'username', 'email', 'name', 'joined_date', 'is_active', ]