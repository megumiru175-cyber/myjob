from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


def generate_userid():
    return uuid.uuid4().hex[:10]

class CustomUser(AbstractUser):
    userid = models.CharField(max_length=10,unique=True,default=generate_userid,editable=False)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.username

    