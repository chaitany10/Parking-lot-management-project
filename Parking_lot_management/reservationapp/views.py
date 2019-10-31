# Create your views here.
import datetime
from datetime import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from parkingapp.models import parkingLot, block, floor, parking_slot
from django.shortcuts import render


from .models import parking_slot_reservation, parking_slip


def confirmbooking(request, parking_lot_no, block_no, floor_no, parking_slot_no):
    if request.user.is_authenticated:
        # final_parking_slot = parkingLot.objects.get(parking_lot_id=parking_lot_no)
        # final_parking_slot = block.objects.get(block_id=block_no, parking_lot_id=final_parking_slot)
        # final_parking_slot = floor.objects.get(floor_id=floor_no, block_id=final_parking_slot)
        # final_parking_slot = parking_slot.objects.get(parking_slot_id=parking_slot_id, floor_id=final_parking_slot)
        # final_parking_slot.is_reserved = True
        # user = request.user.username
        # parking_slot_reservation.customer_id = user
        # parking_slot_reservation.parking_slot_id = final_parking_slot
        # # parking_slot_reservation.duration_in_minutes = duration
        # parking_slot_reservation.save()
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
        # final_parking_slot1 = parkingLot.objects.get(parking_lot_id=parking_lot_no)
        # final_parking_slot2 = block.objects.get(block_id=block_no, parking_lot_id=final_parking_slot1)
        # final_parking_slot3 = floor.objects.get(floor_id=floor_no, block_id=final_parking_slot2)
        # final_parking_slot4 = parking_slot.objects.get(parking_slot_id=parking_slot_no, floor_id=final_parking_slot3)
        # final_parking_slot4.is_reserved = True
        user = request.user.username
        parking_slot_reservation.customer_id = user
        # parking_slot_reservation.parking_slot_id = final_parking_slot
        # parking_slot_reservation.duration_in_minutes = duration
        parking_slot_reservation.save()
        context = {
            'parking_lot_no': parking_lot_no,
            'block_no': block_no,
            'floor_no': floor_no,
            'parking_slot_no': parking_slot_no,

        }
        return render(request, 'parking_lot_index.html', context)
        # return HttpResponseRedirect(reverse('parking_slip'), parking_slot_reservation)
    else:
        return HttpResponseRedirect(reverse('home'))


def print_parking_slip(request, parking_slot_reservation):
    if request.user.is_authenticated:
        bill = parking_slip()
        bill.actual_exit_time = datetime.now()
