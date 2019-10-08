from django.urls import path, re_path, include
from blogindex import views

urlpatterns = [
    path('base/', views.base),
    path('about/', views.about),#个人简介页面
    path('index/', views.index,name='index'),#博客首页
    path('listpic/', views.listpic),
    re_path('newslistpic/(?P<page>\d+)', views.newslistpic),#文章列表
    path('newslistpic/', views.newslistpic),#文章列表
    path('articletails/', views.articletails),#进入文章详情页
    re_path('articletails/(?P<id>\d+)', views.articletails),#进入文章详情页
    path('ckeditor/',include('ckeditor_uploader.urls')),#富文本编辑器
]
