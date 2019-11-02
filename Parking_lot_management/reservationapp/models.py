from accounts.models import Customer
from django.db import models
from parkingapp.models import parking_slot


# Create your models here.
class parking_slot_reservation(models.Model):
    cost_per_hour = models.IntegerField()
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_time_stamp = models.DateTimeField(auto_now=True)
    duration_in_minutes = models.IntegerField()
    booking_date = models.DateField(auto_now=True)
    parking_slot_id = models.ForeignKey(parking_slot, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class parking_slip(models.Model):
    id = models.AutoField(primary_key=True)
    actual_entry_time = models.DateTimeField(auto_now=True)
    actual_exit_time = models.DateTimeField()
    basic_cost = models.IntegerField()
    is_paid = models.BooleanField(default=True)
    parking_slot_id = models.ForeignKey(parking_slot, on_delete=models.CASCADE)
