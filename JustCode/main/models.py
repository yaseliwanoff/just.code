# from django.db import models
# from django.contrib.auth.models import AbstractUser


# # # Модель пользователя
# # class User(AbstractUser):
# #     photo = models.ImageField(upload_to='user_photos/', null=True, blank=True, verbose_name="Фото пользователя")

# #     class Meta:
# #         verbose_name = "Пользователь"
# #         verbose_name_plural = "Пользователи"


# # Абстрактная модель для общей логики
# class BaseContent(models.Model):
#     class ProductCategory(models.TextChoices):
#         # Доделать категории
#         CAR = "Car"
#         COMPUTER = "Computer"
#         LAPTOP = "Laptop"
#         PHONE = "Phone"
#         HOUSE = "House"
#         OTHER = "Other"

#     class ProductStatus(models.TextChoices):
#         PUBLISHED = "PB", "Published"
#         DRAFT = "DR", "Draft"

#     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
#     photo = models.ImageField(upload_to='content_photos/', null=True, blank=True, verbose_name="Фото автора")
#     category = models.CharField()  # Доделать Foreign Key
#     tags = models.CharField(max_length=255, verbose_name="Теги")
#     name = models.CharField(max_length=255, verbose_name="Имя")
#     views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

#     class Meta:
#         abstract = True


# # Модель для статьи
# class Article(BaseContent):
#     short_description = models.TextField(verbose_name="Краткое описание")
#     detailed_description = models.TextField(verbose_name="Подробное описание")

#     class Meta:
#         verbose_name = "Статья"
#         verbose_name_plural = "Статьи"


# # Модель для новостей
# class News(BaseContent):
#     description = models.TextField(verbose_name="Описание")

#     class Meta:
#         verbose_name = "Новость"
#         verbose_name_plural = "Новости"


# # Модель для ошибок и багов
# class Bug(BaseContent):
#     short_description = models.TextField(verbose_name="Краткое описание")
#     detailed_description = models.TextField(verbose_name="Подробное описание")

#     class Meta:
#         verbose_name = "Ошибка или баг"
#         verbose_name_plural = "Ошибки и баги"
