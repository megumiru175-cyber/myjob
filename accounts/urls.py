from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("",LoginView.as_view(template_name="accounts/login.html"),name="login"),

    path(
        "login/",LoginView.as_view(template_name="accounts/login.html"),name="login_page"),

    path("new/", views.new_view, name="new"),

    path("logout/",LogoutView.as_view(),name="logout",),
]