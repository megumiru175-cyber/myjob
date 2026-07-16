from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo
from django.shortcuts import render

class actionView(View):
    def get(self,request):
        page_list = Page.objects.order_by("action")
        return render(request,"action/touch.html",{"touch":actionView}) 