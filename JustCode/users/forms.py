from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import UserCustomModel


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserCustomModel
        fields = ["username", "first_name", "last_name", "email", "date_birch"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Емаил"}),
            "date_birch": forms.DateInput(attrs={"class": "form-control", "placeholder": "Дата рождения", "type": "date"}),
        }
        labels = {
            "username": "Логин",
            "first_name": "Имя пользователя",
            "last_name": "Фамилия пользователя",
            "email": "Емаил пользователя",
            "date_birch": "Дата рождения пользователя",
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))

    class Meta:
        model = UserCustomModel
        fields = ["username", "password"]
