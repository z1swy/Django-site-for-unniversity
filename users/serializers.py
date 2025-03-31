
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['patronymic'] = user.patronymic
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['group_number'] = user.group_number
        # ...

        return token
class CustomUserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail", read_only=True)
    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'patronymic', 'phone_number', 'group_number']
