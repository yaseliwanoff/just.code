from django import forms
from .models import Article, News, Bug


# Форма для создания статьи
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['tags', 'name', 'short_description', 'detailed_description']
        widgets = {
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги статьи'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя статьи'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Полное описание'}),
        }
        labels = {
            'tags': 'Теги статьи',
            'name': 'Имя статьи',
            'short_description': 'Краткое описание',
            'detailed_description': 'Полное описание',
        }


# Форма для создания новости
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['tags', 'name', 'description']
        widgets = {
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги новости'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя новости'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
        }
        labels = {
            'tags': 'Теги новости',
            'name': 'Имя новости',
            'description': 'Описание',
        }


# Форма для создания ошибки или бага
class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['tags', 'name', 'short_description', 'detailed_description']
        widgets = {
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги публикации'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя публикации'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Полное описание'}),
        }
        labels = {
            'tags': 'Теги публикации',
            'name': 'Имя публикации',
            'short_description': 'Краткое описание',
            'detailed_description': 'Полное описание',
        }
