from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField('Пользователь', blank=True, null=True, max_length=50 )
    email = models.EmailField('Почта', unique=True,)
    tel = models.CharField('Телефон', max_length=16, blank=True, null=True)
    is_client = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tel', 'is_client']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

