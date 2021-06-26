from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    username = models.CharField(
        'username', unique=True, blank=False, max_length=50)
    email = models.EmailField('email', unique=True, blank=False)
    first_name = models.CharField('first name', max_length=150, blank=False)
    role = models.CharField(
        'role', max_length=10, choices=Role.choices, default=Role.USER)

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    def __str__(self):
        return self.username
