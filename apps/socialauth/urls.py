from django.urls import path,re_path
from django.urls import re_path as url
from . views import login_page, register_page

urlpatterns = [
    path('', login_page, name='login_url'),
    path('register/', register_page, name='register_url'),


    ]