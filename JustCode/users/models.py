import uuid

from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, first_name, last_name, date_birch, password=None, **more_fields):
        if not email:
            raise ValueError('Error: Your account must have an email.')
        if not username or not first_name or not last_name:
            raise ValueError('Error: Your account must have personal information parameters.')
        
        email = self.normalize_email(email)
        account = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            date_birch=date_birch,
            password=password,
            **more_fields
        )
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_user(self, email, username, first_name, last_name, date_birch, password=None, **more_fields):
        more_fields.setdefault('is_superuser', False)
        more_fields.setdefault('is_staff', False)
        more_fields.setdefault('is_active', True)

        if more_fields.get('is_superuser') is not False or more_fields.get('is_staff') is not False:
            raise ValueError('Error! Just user has have NO superuser and No staff')
        elif more_fields.get('is_active', True) is not True:
            raise ValueError('Active user has no True')
        else:
            return self._create_user(email, username, first_name, last_name, date_birch, password=password, **more_fields)

    def create_superuser(self, email, username, first_name, last_name, date_birch, password=None, **more_fields):
        more_fields.setdefault('is_superuser', True)
        more_fields.setdefault('is_staff', True)
        more_fields.setdefault('is_active', True)

        if more_fields.get('is_superuser', True) is not True:
            raise ValueError('Error is superuser no True')
        elif more_fields.get('is_active', True) is not True:
            raise ValueError('Error is active no True')
        elif more_fields.get('is_staff', True) is not True:
            raise ValueError('Error is staff no True')
        else:
            return self._create_user(email, username, first_name, last_name, date_birch, password=password, **more_fields)


class UserCustomModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='Username',
                                default='username', error_messages={'unique': 'A user with that username already exists.'})
    user_slug = models.SlugField(max_length=100, blank=False, null=False, verbose_name='Slug',
                                 unique=True, error_messages={'unique': 'A user with that user slug already exists.'})
    account_photo = models.ImageField(upload_to='account_photos/', null=True, blank=True, verbose_name="User photo")
    first_name = models.CharField(max_length=60, null=False, blank=False, verbose_name='First name')
    last_name = models.CharField(max_length=60, null=False, blank=False, verbose_name='Last name')
    description_account = models.TextField(max_length=5000, null=False, blank=False, verbose_name='Profile description')
    email = models.EmailField(null=False, blank=False, verbose_name='Email for account', unique=True,
                              error_messages={'unique': 'A user with that username already exists.'})
    phone = models.PositiveIntegerField(null=True, blank=True, verbose_name='phone number')
    date_birch = models.DateTimeField(null=False, blank=False, verbose_name="User birch", editable=True)
    create_account = models.DateTimeField(auto_now_add=True, verbose_name='Time create account')

    is_active = models.BooleanField(default=True, verbose_name='Is Active?')
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff?')
    is_superuser = models.BooleanField(default=False, verbose_name='Is Superuser?')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"id: {self.id} username: {self.useranme} email: {self.email} | first name: {self.first_name} last name: {self.last_name}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['create_account']
        indexes = [
            models.Index(fields=['create_account'])
        ]

