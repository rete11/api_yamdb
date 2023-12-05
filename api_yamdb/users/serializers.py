import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'bio',
            'role',
        )


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    username = serializers.CharField(max_length=150)

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def validate_username(self, value):
        if not re.findall(r'^[\w.@+-]+\Z', value) or value == 'me':
            raise ValidationError('Некорректное имя.')
        return value


class TokenSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(required=True)
    username = serializers.CharField(max_length=150)

    class Meta:
        model = CustomUser
        fields = ('username', 'confirmation_code')
