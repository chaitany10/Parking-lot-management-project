from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
#from carposition.models import Positions
from .models import Customer
from .forms import LoginForm, RegForm
from django.conf import settings
#from tariff.models import Tariffs
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        print("Hello ")
        if reg_form.is_valid():
            print("Hello")
            customer =Customer()
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # Create user

            user = User.objects.create_user(username, email, password)
            print(user.username)
            user.save()
            # Login user
            customer.firstname = reg_form.cleaned_data['firstname']
            customer.lastname = reg_form.cleaned_data['lastname']
            customer.phone = reg_form.cleaned_data['user_phone']
            customer.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect(request.GET.get('from', reverse('user_detail')))
        print("This place reached " + str(reg_form.errors))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)


# @login_required
# def user_detail(request):
#     if request.method == 'POST':
#         user_form = UserDetailForm(request.POST)
#         if user_form.is_valid() and (request.user is not None):
#             # Add user information
#             # print("Hello")
#             user_info = UserInfo()
#             # print("Hi")
#             user_info.user_name = request.user.username
#             # user_info.user_name = user_form.cleaned_data['user_name']
#             # user_info.user_first_name= user_form.cleaned_data['user_first_name']
#             user_info.user_phone = user_form.cleaned_data['user_phone']
#             user_info.car_number = user_form.cleaned_data['car_number']
#             user_info.car_type = user_form.cleaned_data['car_type']
#             # user_info.car_color = user_form.cleaned_data['car_color']
#             # user_info.car_kind = user_form.cleaned_data['car_kind']
#             user_info.save()
#         return redirect(request.GET.get('from', reverse('home')))
#     else:
#         user_form = UserDetailForm()
#     context = {}
#     context['user_form'] = user_form
#     return render(request, 'user_detail.html', context)
#
#
# @login_required
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(settings.LOGIN_URL)
#
#
# def Checkoutuser(request):
#     if not request.user.is_site_manager:
#         return redirect('/users/home')
#
#     UserInfolist = UserInfo.objects.values()
#
#     # print(UserInfolist)
#     context = {
#         'UserInfolist': UserInfolist
#     }
#
#     return render(request, 'Checkoutuser.html', context)
#

