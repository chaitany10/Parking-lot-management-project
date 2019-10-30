# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from datetime import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from parkingapp.models import parkingLot, block, floor

from .models import parking_slot_reservation, parking_slip


def reserve(request,parking_lot_no,block_no,floor_no, parking_slot_id):
    if request.user.is_authenticated:
        final_parking_slot = parkingLot.objects.get(parking_lot_id = parking_lot_no)
        final_parking_slot = block.objects.get(block_id = block_no)
        final_parking_slot = floor.objects.get(floor_id=floor_no)
        final_parking_slot = parking_slot.objects.get(parking_slot_id=parking_slot_id)
        # final_parking_slot.isbooked= True
        user = request.user.username
        parking_slot_reservation.customer_id = user
        parking_slot_reservation.parking_slot_id = final_parking_slot.parking_slot_id
        # parking_slot_reservation.duration_in_minutes = duration
        parking_slot_reservation.save()
        return HttpResponseRedirect(reverse('parking_slip'), parking_slot_reservation)
    else:
        return HttpResponseRedirect(reverse('home'))

def print_parking_slip(request, parking_slot_reservation):
    if request.user.is_authenticated:
        bill = parking_slip()
        bill.actual_exit_time = datetime.now()


