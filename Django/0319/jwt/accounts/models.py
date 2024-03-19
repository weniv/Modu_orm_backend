from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

GENDER_CHOICES = (
    ("male", "남자"),
    ("female", "여자"),
)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
