from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    email = models.EmailField('email', unique=True, blank=False)
    username = models.CharField(
        'username', unique=True, blank=False, max_length=50)
    role = models.CharField(
        'role', max_length=10, choices=Role.choices, default=Role.USER)

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser
