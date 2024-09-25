# views.py
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from users.models import UserCustomModel as User
from .models import Article
from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, JustSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Представление для регистрации новых пользователей
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # Кастомное представление для получения JWT токена
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

class JustAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class JustAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = JustSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = JustAPIListPagination

    # изменение
class JustAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = JustSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )

    # удаление чтение админ и обынчый
class JustAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = JustSerializer
    permission_classes = (IsAdminOrReadOnly,)


