from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser

from user.managers import UserManager


class User(AbstractUser):
    """Username replace with email, first_name, last_name = required"""
    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,

    )
    first_name = models.CharField(
        _("first name"),
        max_length=150
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
