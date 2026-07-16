from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


from django.urls import path
from . import views

app_name="action"

urlpatterns = [
    path("", views.touch, name="touch"),
]
