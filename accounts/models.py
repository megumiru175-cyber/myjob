from django.db import models
from django.contrib.auth.models import AbstractUser

class  CustomUser(AbstractUser):
    userid = models.CharField(max_length=10, unique=True, blank=True)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
