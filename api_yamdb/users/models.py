from django.db import models
from django.contrib.auth.models import AbstractUser


USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'

ROLES = (
    (USER, 'User'),
    (ADMIN, 'Moderator'),
    (MODERATOR, 'Admin'),
)


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    bio = models.TextField(max_length=500, blank=True, null=True)
    role = models.CharField(
        max_length=70,
        choices=ROLES,
        default=USER,
        blank=True,
    )
    confirmation_code = models.TextField(
        unique=True,
        blank=True,
        null=True,
    )

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR or self.is_admin

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
