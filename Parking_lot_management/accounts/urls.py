from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns =[
    path('login/',views.login,name = 'login'),
    path('register/',views.register,name = 'register')
]