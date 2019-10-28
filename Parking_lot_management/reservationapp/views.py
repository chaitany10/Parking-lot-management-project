from django.shortcuts import render
from .models import parking_slot_reservation, parking_slip
# Create your views here.
from accounts.models import Customer
from parkingapp.models import parking_slot
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def reserve(request, parking_slot_id, duration):
    if request.user.is_authenticated:
        parking_slot_reservation = parking_slot()
        user = request.user.username
        parking_slot_reservation.customer_id =user
        parking_slot_reservation.parking_slot_id = parking_slot_id
        parking_slot_reservation.duration_in_minutes = duration
        parking_slot_reservation.save()
        return HttpResponseRedirect(reverse('parking_slip'), parking_slot_reservation)
    else:
        return HttpResponseRedirect(reverse('home'))

def print_parking_slip(request, parking_slot_reservation):
    bill = parking_slip()
