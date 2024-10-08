# Generated by Django 4.2 on 2024-08-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2, verbose_name='Статус публикации')),
                ('type_status', models.CharField(choices=[('Статьи', 'Статьи'), ('Новости', 'Новости'), ('Ошибки и баги', 'Ошибки и баги')], default='Статьи', max_length=20, verbose_name='Тип публикации')),
                ('category', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('DevOps', 'DevOps'), ('JavaScript', 'JavaScript'), ('Algorithms', 'Algorithms'), ('Sql', 'Sql'), ('React', 'React'), ('Vue', 'Vue'), ('Angular', 'Angular'), ('Django', 'Django'), ('FastApi', 'FastApi'), ('C#', 'C#'), ('C++', 'C++'), ('Математика', 'Математика')], default='Frontend', max_length=20, verbose_name='Теги публикации')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='content_photos/', verbose_name='Фото автора')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('detailed_description', models.TextField(verbose_name='Подробное описание')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2, verbose_name='Статус публикации')),
                ('type_status', models.CharField(choices=[('Статьи', 'Статьи'), ('Новости', 'Новости'), ('Ошибки и баги', 'Ошибки и баги')], default='Статьи', max_length=20, verbose_name='Тип публикации')),
                ('category', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('DevOps', 'DevOps'), ('JavaScript', 'JavaScript'), ('Algorithms', 'Algorithms'), ('Sql', 'Sql'), ('React', 'React'), ('Vue', 'Vue'), ('Angular', 'Angular'), ('Django', 'Django'), ('FastApi', 'FastApi'), ('C#', 'C#'), ('C++', 'C++'), ('Математика', 'Математика')], default='Frontend', max_length=20, verbose_name='Теги публикации')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='content_photos/', verbose_name='Фото автора')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('detailed_description', models.TextField(verbose_name='Подробное описание')),
            ],
            options={
                'verbose_name': 'Ошибка или баг',
                'verbose_name_plural': 'Ошибки и баги',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2, verbose_name='Статус публикации')),
                ('type_status', models.CharField(choices=[('Статьи', 'Статьи'), ('Новости', 'Новости'), ('Ошибки и баги', 'Ошибки и баги')], default='Статьи', max_length=20, verbose_name='Тип публикации')),
                ('category', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('DevOps', 'DevOps'), ('JavaScript', 'JavaScript'), ('Algorithms', 'Algorithms'), ('Sql', 'Sql'), ('React', 'React'), ('Vue', 'Vue'), ('Angular', 'Angular'), ('Django', 'Django'), ('FastApi', 'FastApi'), ('C#', 'C#'), ('C++', 'C++'), ('Математика', 'Математика')], default='Frontend', max_length=20, verbose_name='Теги публикации')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='content_photos/', verbose_name='Фото автора')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
