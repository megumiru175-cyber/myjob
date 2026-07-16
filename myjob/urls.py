from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


from django.urls import path
from . import views

app_name="myjob"

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("touch/", views.touch, name="touch"),
    path("page/create/",views.page_create,name ="page_create"),
    path("page/",views.page_list,name="page_list"),
    path("page/<uuid:id>/", views.page_detail,name="page_detail"),
    path("page/<uuid:id>/upload", views.page_update,name="page_update"),
    path("page/<uuid:id>/delete", views.page_delete,name="page_delete"),
    path('comment/create/<uuid:id>/', views.CommentView.as_view(), name='comment')
]