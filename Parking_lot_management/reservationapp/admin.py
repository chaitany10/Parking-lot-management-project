from django.contrib import admin

from .models import parking_slot_reservation, parking_slip


# Register your models here.
@admin.register(parking_slot_reservation)
class parkingLotAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'start_time_stamp', 'duration_in_minutes', 'booking_date', 'parking_slot_id')


@admin.register(parking_slip)
class blockAdmin(admin.ModelAdmin):
    list_display = ('id', 'actual_entry_time', 'actual_exit_time', 'basic_cost', 'is_paid', 'parking_slot_id')
