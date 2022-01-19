from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField('Пользователь', blank=True, null=True, max_length=50 )
    email = models.EmailField('Почта', unique=True,)
    tel = models.CharField('Телефон', max_length=16, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

