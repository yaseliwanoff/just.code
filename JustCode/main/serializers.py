# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Сериализатор для модели пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')  # Поля, которые будут включены в сериализацию
        extra_kwargs = {'password': {'write_only': True}}  # Указание, что поле пароля только для записи

    def create(self, validated_data):
        # Создание нового пользователя с зашифрованным паролем
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

# Кастомный сериализатор для получения JWT токена
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        # Добавление дополнительных претензий в токен
        token['username'] = user.username
        return token
