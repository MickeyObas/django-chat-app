from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        ordering = ['email']

    def __str__(self):
        return self.email


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
