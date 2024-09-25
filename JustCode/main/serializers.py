from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from main.models import Article
from users.models import UserCustomModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'date_birch')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserCustomModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_birch=validated_data['date_birch'],
            password=validated_data['password']
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


class JustSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ('__all__')