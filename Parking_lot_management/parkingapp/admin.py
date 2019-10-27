from django.contrib import admin

from .models import parkingLot, block, floor, parking_slot


# Register your models here.
@admin.register(parkingLot)
class parkingLotAdmin(admin.ModelAdmin):
    list_display = (
    'is_slot_available', 'is_reentry_allowed', 'no_of_blocks', 'pincode', 'is_valet_available', 'landmark',
    'building_no', 'street_name')


@admin.register(block)
class blockAdmin(admin.ModelAdmin):
    list_display = ('parking_lot_id', 'is_block_full', 'no_of_floors', 'block_code')


@admin.register(floor)
class floorAdmin(admin.ModelAdmin):
    list_display = (
    'block_id', 'is_floor_full', 'is_covered', 'floor_number', 'max_height', 'no_of_slots', 'no_of_wings', 'block_code')


@admin.register(parking_slot)
class parking_slotAdmin(admin.ModelAdmin):
    list_display = ('floor_id', 'wing_code', 'slot_no')
