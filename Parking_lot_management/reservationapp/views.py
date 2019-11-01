# Create your views here.
import datetime
from datetime import datetime

from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .forms import DurationForm
from .models import parking_slip


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
        form = DurationForm()
        context = {
            'parking_lot_no': parking_lot_no,
            'block_no': block_no,
            'floor_no': floor_no,
            'parking_slot_no': parking_slot_no,
            'form': form

        }
        return render(request, 'confirmbooking.html', context)
        # return HttpResponseRedirect(reverse('parking_slip'), parking_slot_reservation)
    else:
        return HttpResponseRedirect(reverse('home'))


def reserve(request, parking_lot_no, block_no, floor_no, parking_slot_no):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DurationForm(request.POST)
            duration = int(request.POST.get('duration', None))
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
            return render(request, 'confirmed.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))


def print_parking_slip(request, parking_slot_reservation):
    if request.user.is_authenticated:
        bill = parking_slip()
        bill.actual_exit_time = datetime.now()
