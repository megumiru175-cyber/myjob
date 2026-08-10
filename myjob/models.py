from django.db import models
from django.contrib.auth.models import AbstractUser
from pathlib import Path
import uuid
from django.utils import timezone
from django.conf import settings


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    text = models.TextField()


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
        related_name="comments")
    user_name = models.CharField("名前", max_length=255, default="NONAME")
    message = models.TextField("本文")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Edit(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50, blank=True,verbose_name="表示名")
    birth_date = models.DateField(null=True, blank=True,verbose_name="誕生日")
    like = models.TextField(max_length=500, blank=True,verbose_name="趣味、好きなもの")

    def __str__(self):
        return self.bio