import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True, default=None)
    is_critic = models.BooleanField(blank=True, null=True, default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("username",)
