from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
import uuid
from django.utils import timezone
from django.contrib.auth.models import ippanUser
from django.db import models


class User(ippanUser):
  is_kannri = models.BooleanField(default=False)
  is_ippan = models.BooleanField(default=False)


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,verbose_name="ID")
    title = models.CharField(max_length=100,verbose_name="タイトル")
    body = models.TextField(max_length=2000,verbose_name="本文")
    Page_date = models.DateField(verbose_name="日付")
    picture = models.ImageField(upload_to="myjob/piture/",blank=True,null = True,verbose_name="画像")
    created_at= models.DateField(auto_now_add=True,verbose_name="作成日時")
    updated_at = models.DateField(auto_now=True,verbose_name="更新日時")

class Comment(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user_name = models.CharField("名前", max_length=255, default="NONAME")
    message = models.TextField("本文")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name