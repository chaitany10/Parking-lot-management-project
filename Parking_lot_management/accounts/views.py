from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, RegForm
# from carposition.models import Positions
from .models import Customer,Vehicle_Numbers


# from tariff.models import Tariffs


def home(request):
    # print("HI")

    # car_positions =Positions.objects.filter(position_status=True)
    # car_pos_num = car_positions.count()
    # print(request.user.is_accountant)
    # print(request.user.is_site_manager)
    #if request.user.is_authenticated and not request.user.is_superuser and not request.user.is_accountant and not request.user.is_site_manager:
    print(request.user)
    customer = Customer.objects.get(email_address=request.user.email)
    context = {
        'firstname': customer.firstname,
        'lastname': customer.lastname,
    }
    # else:
    #     context = {
    #         'car_pos_num' : car_pos_num
    # }
    print("Rendering home")
    return render(request, 'home.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            login(request, user)
            if user is not None:
                # request.session['alert_success'] = "Successfully logged in."
                return HttpResponseRedirect('/home/')
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
            customer = Customer()
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # Create user
            vehicle = Vehicle_Numbers()
            user = User.objects.create_user(username, email, password)
            print(user.username)
            user.save()
            # Login user
            customer.firstname = reg_form.cleaned_data['firstname']
            customer.lastname = reg_form.cleaned_data['lastname']
            customer.phone = reg_form.cleaned_data['user_phone']
            vehicle.vehicle_no = reg_form.cleaned_data['car_number']
            vehicle.customer_id = Customer.objects.get(phone = customer.phone)
            customer.save()
            vehicle.save()

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
