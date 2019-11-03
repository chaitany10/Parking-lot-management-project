import json
import urllib

from django.conf import settings
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from tariff.models import Tariffs
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from parkingapp.models import parking_slot
from reservationapp.models import parking_slot_reservation

from .forms import LoginForm, RegForm
# from carposition.models import Positions
from .models import Customer, Vehicle_Numbers, Regular_Customer


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def profile(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(customer_id=request.user)
        regular = Regular_Customer.objects.filter(customer_id=customer)
        vehicle = Vehicle_Numbers.objects.get(customer_id=customer)
        context = {
            'customer': customer,
            'regular': regular,
            'vehicle': vehicle
        }
        return render(request, 'profile.html', context)
    else:
        context = {

        }
    return HttpResponseRedirect(reverse('login'))


def home(request):
    # print("HI")
    print('in home')

    # car_positions =Positions.objects.filter(position_status=True)
    # car_pos_num = car_positions.count()
    # print(request.user.is_accountant)
    # print(request.user.is_site_manager)
    current_booking = True
    customer = Customer.objects.get(customer_id=request.user)
    reservation = parking_slot_reservation.objects.get(customer_id=customer, is_active=True)
    if reservation is None:
        current_booking = False

    if request.user.is_authenticated and not request.user.is_superuser:
        print(request.user)

        customer = Customer.objects.get(customer_id=request.user)
        context = {
            'customer': customer,
            'current_booking': current_booking
        }
    else:
        context = {

        }
    print("Rendering home")
    return render(request, 'home.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                user = authenticate(
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password']
                )
                login(request, user)
                if user is not None:
                    return HttpResponseRedirect('/home/')


            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)


@csrf_exempt
def register(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
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
            user = User.objects.create_user(username=username, email=email, password=password)
            print(user.username)
            user1 = authenticate(
                username=reg_form.cleaned_data['username'],
                password=reg_form.cleaned_data['password']
            )
            login(request, user1)
            # if request.user.is_authenticated:
            #     print('inside is auth')
            customer.firstname = reg_form.cleaned_data['firstname']
            customer.lastname = reg_form.cleaned_data['lastname']
            customer.phone = reg_form.cleaned_data['user_phone']
            customer.customer_id = reg_form.cleaned_data['username']
            customer.save()
            customer1 = Customer.objects.get(customer_id=username)
            vehicle = Vehicle_Numbers()
            vehicle.customer_id = customer1
            vehicle.vehicle_no = reg_form.cleaned_data['car_number']

            vehicle.save()

            return HttpResponseRedirect(reverse('home'))

        print("This place reached " + str(reg_form.errors))
    else:
        reg_form = RegForm()

    context['form'] = reg_form
    return render(request, 'register.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def bookingHistory(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
        customer = Customer.objects.get(customer_id=request.user)
        current_reservation = parking_slot_reservation.objects.get(customer_id=customer, is_active=True)
        past_reservation = parking_slot_reservation.objects.get(customer_id=customer, is_active=False)
        context = {
            'customer': customer,
            'past': past_reservation,
            'current': current_reservation
        }


def checkout(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        customer = Customer.objects.get(customer_id=request.user)
        reservation = parking_slot_reservation.objects.get(customer_id=customer, is_active=True)
        reservation.is_active = False
        cost_per_hour = reservation.cost_per_hour
        parking_slot1 = parking_slot.objects.get(id=reservation.parking_slot_id.id)
        parking_slot1.is_reserved = False
        parking_slot1.save()
        total_duration = 1
        total_cost = total_duration * cost_per_hour

        context = {
            'reservation': reservation,
            'customer': customer,
            'total_cost': total_cost
        }
        reservation.save()

        return render(request, 'checkout.html', context)
