from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home' ),
    path('blog-1', views.blog_detail1,name='blog_detail1' ),
    path('blog-2', views.blog_detail2,name='blog_detail2' ),
    path('blog-3', views.blog_detail3,name='blog_detail3' ),
]
