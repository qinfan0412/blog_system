from django.urls import path, re_path
from management.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    re_path('^$', login),
    path('index/', index),
    path('base/', base),
    path('list/', list),
    path('list/', list),
    path('personal_info/', personal_info),
    path('article_add/', article_add),
    path('article_update/', article_update),
    re_path('list/(?P<page>\d+)', list),
    # path('personal_info/', personal_info),
]