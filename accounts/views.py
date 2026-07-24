from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

# カスタムユーザーを取得
User = get_user_model()

def users_view(request):
    users = User.objects.all()

    context = {
        'users' : users
    }

    return render(request, '', context)