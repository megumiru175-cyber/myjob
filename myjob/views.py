from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Page,Comment,Edit
from .forms import PageForm,CommentForm,EditForm
from datetime import datetime
from zoneinfo import ZoneInfo
from django.views.generic import TemplateView, CreateView
from django.urls import reverse
from .forms import PageForm, CommentForm,EditForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class IndexView(LoginRequiredMixin,View):
     def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request, "myjob/index.html",{"datetime_now":datetime_now})
     

class MenuView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request, "myjob/menu.html")
   
class TouchView(LoginRequiredMixin,View):
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

class PageDetailView(LoginRequiredMixin,View):
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
    
class CommentView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        page = get_object_or_404(Page, pk=self.kwargs["id"])
        form.instance.page = page
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("myjob:page_detail", kwargs={"id": self.kwargs["id"]})


class MypageView(LoginRequiredMixin,TemplateView):
    template_name = "myjob/mypage.html"
    def get_context_data(self, **kwargs):
        # 継承元であるTemplateViewのget_context_data()メソッド
        context = super().get_context_data(**kwargs)
        edit, created = Edit.objects.get_or_create(user=self.request.user)
        context["edit"] = edit
        return context


@login_required
def edit_profile(request):
    profile, created = Edit.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("myjob:mypage")
    else:
        form = EditForm(instance=profile)

    return render(request, "myjob/editprofile.html", {"form": form})
    
index = IndexView.as_view()
menu = MenuView.as_view()
touch = TouchView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
comment= CommentView.as_view()
mypage = MypageView.as_view()
