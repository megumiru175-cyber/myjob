from django.forms import ModelForm
from .models import Page
from .models import Comment
from django import forms
from django.forms import ModelForm
from .models import Page
from .models import Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [User.USERNAME_FIELD] + User.REQUIRED_FIELDS

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields=  "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "message"]