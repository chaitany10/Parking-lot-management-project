from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('profile/',views.profile,name='profile')
]
