from django.db import models


# Create your models here.
class parkingLot(models.Model):
    parking_lot_id = models.AutoField(unique=True, primary_key=True)
    is_slot_available = models.BooleanField(default=True)
    is_reentry_allowed = models.BooleanField(default=False)
    no_of_blocks = models.IntegerField(default=1)
    pincode = models.IntegerField()
    is_valet_available = models.BooleanField(default=False)
    landmark = models.CharField(max_length=30)
    building_no = models.IntegerField()
    street_name = models.CharField(max_length=30)


class block(models.Model):
    parking_lot_id = models.ForeignKey(parkingLot, on_delete=models.CASCADE)
    block_id = models.AutoField(unique=True, primary_key=True)
    is_block_full = models.BooleanField(default=False)
    no_of_floors = models.IntegerField(default=1)
    block_code = models.CharField(max_length=30)


class floor(models.Model):
    block_id = models.ForeignKey(block, on_delete=models.CASCADE)
    floor_id = models.AutoField(unique=True, primary_key=True)
    is_floor_full = models.BooleanField(default=False)
    is_covered = models.BooleanField(default=False)
    floor_number = models.AutoField(unique=True, primary_key=True)
    max_height = models.IntegerField()
    no_of_slots = models.IntegerField(default=1)
    no_of_wings = models.IntegerField(default=1)
    block_code = models.CharField(max_length=30)


class parking_slot(models.Model):
    floor_id = models.ForeignKey(floor, on_delete=models.CASCADE)
    parking_slot_id = models.AutoField(unique=True, primary_key=True)
    wing_code = models.CharField(max_length=10)
    slot_no = models.IntegerField(default=1)
