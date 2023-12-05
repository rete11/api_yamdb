from rest_framework import serializers

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

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class TokenSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'confirmation_code')
