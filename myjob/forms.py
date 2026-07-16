from django.forms import ModelForm
from .models import Page
from .models import Comment
from django import forms
from django.forms import ModelForm
from .models import Page
from .models import Comment


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields=  "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "message"]