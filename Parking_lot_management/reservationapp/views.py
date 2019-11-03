# Create your views here.
import datetime
from datetime import datetime
from accounts.models import Customer
from parkingapp.models import parkingLot,block,floor,parking_slot
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .forms import DurationForm
from .models import parking_slip,parking_slot_reservation


def confirmbooking(request, parking_lot_no, block_no, floor_no, parking_slot_no):
    if request.user.is_authenticated:


        context = {
            'parking_lot_no': parking_lot_no,
            'block_no': block_no,
            'floor_no': floor_no,
            'parking_slot_no': parking_slot_no,

        }
        return render(request, 'confirmbooking.html', context)
        # return HttpResponseRedirect(reverse('parking_slip'), parking_slot_reservation)
    else:
        return HttpResponseRedirect(reverse('home'))


def reserve(request, parking_lot_no, block_no, floor_no, parking_slot_no):
    if request.user.is_authenticated:
        parking_lot = parkingLot.objects.get(parking_lot_id=parking_lot_no)
        block1 = block.objects.get(parking_lot_id=parking_lot, id=block_no)
        floor1 = floor.objects.get(id=floor_no, block_id=block1)
        final_parking_slot = parking_slot.objects.get(id=parking_slot_no, floor_id=floor1)
        final_parking_slot.is_reserved = True
        final_parking_slot.save()
        customer = Customer.objects.get(customer_id=request.user)
        parking_slot_reservation1 = parking_slot_reservation()
        parking_slot_reservation1.customer_id = customer
        parking_slot_reservation1.parking_slot_id = final_parking_slot
        parking_slot_reservation1.cost_per_hour = parking_lot.cost
        parking_slot_reservation1.cost = parking_lot.cost
        parking_slot_reservation1.save()
        context = {
            'parking_lot_no': parking_lot_no,
            'block_no': block_no,
            'floor_no': floor_no,
            'parking_slot_no': parking_slot_no,
        }
        return render(request, 'confirmed.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))

