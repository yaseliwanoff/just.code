from rest_framework import serializers
from users.models import UserCustomModel

from rest_framework import serializers
from .models import UserCustomModel


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserCustomModel
        fields = ["id", "username", "first_name", "last_name", "email", "date_birch", "password"]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        # Проверка уникальности имени пользователя и email
        if UserCustomModel.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username": "Этот логин уже занят."})
        if UserCustomModel.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Этот email уже зарегистрирован."})

        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user