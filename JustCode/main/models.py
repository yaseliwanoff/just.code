from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import UserCustomModel


# # Модель пользователя
# class User(AbstractUser):
#     photo = models.ImageField(upload_to='user_photos/', null=True, blank=True, verbose_name="Фото пользователя")

#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"


# Абстрактная модель для общей логики
class BaseContent(models.Model):
    class ProductCategory(models.TextChoices):
        FRONTEND = "Frontend", "Frontend"
        BACKEND = "Backend", "Backend"
        FULLSTACK = "Fullstack", "Fullstack"
        DEVOPS = "DevOps", "DevOps"
        JAVASCRIPT = "JavaScript", "JavaScript"
        ALGORITHMS = "Algorithms", "Algorithms"
        SQL = "Sql", "Sql"
        REACT = "React", "React"
        VUE = "Vue", "Vue"
        ANGULAR = "Angular", "Angular"
        DJANGO_BEST = "Django", "Django"
        FASTAPI = "FastApi", "FastApi"
        CC = "C#", "C#"
        CCC = "C++", "C++"
        MATH = "Математика", "Математика"

    class ProductStatus(models.TextChoices):
        PUBLISHED = "PB", "Published"
        DRAFT = "DR", "Draft"

    class ProductWherePublish(models.TextChoices):
        ARTICLE = "Статьи", "Статьи"
        NEWS = "Новости", "Новости"
        ERROR_BAGS = "Ошибки и баги", "Ошибки и баги"
    
    status = models.CharField(
        max_length=2,
        choices=ProductStatus.choices,
        default=ProductStatus.DRAFT,
        verbose_name="Статус публикации"
    )
    
    type_status = models.CharField(
        max_length=20,
        choices=ProductWherePublish.choices,
        default=ProductWherePublish.ARTICLE,
        verbose_name="Тип публикации"
    )
    
    category = models.CharField(
        max_length=20,
        choices=ProductCategory.choices,
        default=ProductCategory.FRONTEND,
        verbose_name="Теги публикации"
    )

    author = models.ForeignKey(UserCustomModel, on_delete=models.CASCADE, verbose_name="Автор")
    photo = models.ImageField(upload_to='content_photos/', null=True, blank=True, verbose_name="Фото автора")
    
    name = models.CharField(max_length=255, verbose_name="Имя")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        abstract = True


# Модель для статьи
class Article(BaseContent):
    short_description = models.TextField(verbose_name="Краткое описание")
    detailed_description = models.TextField(verbose_name="Подробное описание")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# Модель для новостей
class News(BaseContent):
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# Модель для ошибок и багов
class Bug(BaseContent):
    short_description = models.TextField(verbose_name="Краткое описание")
    detailed_description = models.TextField(verbose_name="Подробное описание")

    class Meta:
        verbose_name = "Ошибка или баг"
        verbose_name_plural = "Ошибки и баги"
