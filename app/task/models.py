from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


from .manager import CustomUserManager

ROLE_CHOICES =(("USER","user"),("ADMIN","admin"))


class CustomUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=5,choices=ROLE_CHOICES)
    profile = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

