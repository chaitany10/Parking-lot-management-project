from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password/', views.change_password, name='change_password'),
    path('checkout/', views.checkout, name='checkout'),
    path('bookinghistory/', views.bookingHistory, name='bookinghistory'),
    path('downloadbills/', views.download_csv, name='download'),
    path('downloadreservations/', views.download_csv_reservation, name='download_reservation'),
    path('downloadcustomers/', views.download_csv_customers, name='download_reservation'),
]
