from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404,redirect
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# カスタムユーザーを取得

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
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = SignupForm()

    return render(request, "accounts/new.html", {"form": form})

def my_error_handler(request, *args, **kw):
    import sys
    from django.views import debug
    from django.http import HttpResponse
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponse(error_html)
    
   