from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from . import views
from django.urls import path


app_name = "accounts"

urlpatterns = [
    path("new/", views.new_view, name="new"), 
    path("", LoginView.as_view(template_name="myjob/index.html"), name="index"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
]
import django.conf.urls as url
from accounts import views
url.handler500 = views.my_error_handler