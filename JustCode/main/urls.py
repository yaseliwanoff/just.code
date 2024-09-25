from django.urls import path

from main.views import JustAPIList, JustAPIUpdate, JustAPIDestroy
from users import views

app_name = "main"

urlpatterns = [
    path('just/', JustAPIList.as_view()),
    path('just/<int:pk>/', JustAPIUpdate.as_view()),
    path('justdelete/<int:pk>/', JustAPIDestroy.as_view()),
]

