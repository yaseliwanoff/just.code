from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("index/", views.index, name="index"),
]

