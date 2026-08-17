from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404,redirect
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
#

User = get_user_model()



class MySignupView(CreateView):
    template_name = "accounts/signup.html"
    form_class = SignupForm
    success_url = '/accounts/user/'
    
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result
    
class MyUserView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user.username)
        return context

def new_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        print("===== POST開始 =====")
        print(request.POST)
        print("フォーム:", form)
        print("フォーム有効:", form.is_valid())
        print("フォームエラー:", form.errors)

        if form.is_valid():
            try:
                user = form.save()
                print("===== 保存成功 =====")
                print(user)
                return redirect("accounts:login")
            except Exception as e:
                print("===== 保存エラー =====")
                print(type(e).__name__)
                print(e)
                raise

    else:
        form = SignupForm()

    return render(request, "accounts/new.html", {"form": form})


   