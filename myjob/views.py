from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Page,Comment,User
from .forms import PageForm,CommentForm,LoginForm
from datetime import datetime
from zoneinfo import ZoneInfo
from django.views.generic import CreateView
from django.urls import reverse

from django.shortcuts import render

class LoginView(LoginRequiredMixin,View):
    form_class = LoginForm
    template_name = "registration/login.html"

# ここでURLの棲み分けをする
    def get_success_url(self):
        user = User.objects.filter(username=self.request.POST['username'])
        if user.is_employee:
            return reverse('kannri')
        else:
            return reverse('ippan')

class IndexView(LoginRequiredMixin,View):
     def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request, "myjob/index.html",{"datetime_now":datetime_now})
     

class MenuView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "myjob/menu.html")
   
class TouchView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "myjob/touch.html")


class PageCreateView(LoginRequiredMixin,View):
    def get(self,request):
        form =PageForm()
        return render(request,"myjob/page_form.html",{"form": form})
    
    def post(self,request):
        form = PageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("myjob:index")
        return render(request,"myjob/page_form.html",{"form": form})

class PageListView(LoginRequiredMixin,View):
    def get(self,request):
        page_list = Page.objects.order_by("Page_date")
        return render(request,"myjob/page_list.html",{"page_list":page_list})                      

class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)

        comments = page.comments.all()
        form = CommentForm()

        return render(
            request,
            "myjob/page_detail.html",
            {
                "page": page,
                "comments": comments,
                "form": form,
            },
        )
    
class PageUpdateView(LoginRequiredMixin,View):
    def get(self,request,id):
        page = get_object_or_404(Page,id=id)
        form =PageForm(instance=page)        
        return render (request,"myjob/page_upload.html",{"form": form})
    def post(self,request,id):
        page = get_object_or_404(Page,id=id)
        form = PageForm(request.POST,request.FILES,instance=page)
        if form.is_valid:
            form.save()
            return redirect("myjob:page_detail", id=id)
        return render(request,"myjob/page_list.html",{"form": form})
                            


class PageDeleteView(LoginRequiredMixin,View):
    def get(self,request,id):
        page = get_object_or_404(Page,id=id)
        return render(request, "myjob/comment.html",{"page": page})
    def post(self,request,id):
        page = get_object_or_404(Page,id=id)
        page.delete()
        return redirect('myjob:page_list')
    
class CommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        page = get_object_or_404(Page, pk=self.kwargs["id"])
        form.instance.page = page
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("myjob:page_detail", kwargs={"id": self.kwargs["id"]})

index = IndexView.as_view()
menu = MenuView.as_view()
touch = TouchView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
comment= CommentView.as_view()