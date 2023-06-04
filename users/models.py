from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image=models.ImageField(upload_to='profile_pics', default='default_profile.jpg')
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=15,unique=True)
    coach=models.BooleanField(default=False)

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"