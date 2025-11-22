from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name="Аватар", help_text='Загрузите свой аватар')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон', help_text='Введите номер телефона')
    country = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

