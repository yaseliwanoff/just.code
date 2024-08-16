# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, CustomTokenObtainPairView

# Маршруты для API
urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Эндпоинт для получения токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Эндпоинт для обновления токена
    path('api/register/', RegisterView.as_view(), name='register'),  # Эндпоинт для регистрации
]
