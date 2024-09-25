from django.urls import path

from . import views
from .views import RegisterUserView

app_name = 'users'

urlpatterns = [
    path("index/", views.index, name="index"),
    path('register/', RegisterUserView.as_view(), name='register_user'),
]