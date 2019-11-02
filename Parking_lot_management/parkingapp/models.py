from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class parkingLot(models.Model):
    parking_lot_id = models.AutoField(unique=True, primary_key=True)
    is_slot_available = models.BooleanField(default=True)
    is_reentry_allowed = models.BooleanField(default=False)
    no_of_blocks = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    pincode = models.IntegerField(validators=[MinValueValidator(1)])
    is_valet_available = models.BooleanField(default=False)
    landmark = models.CharField(max_length=30)
    building_no = models.IntegerField(validators=[MinValueValidator(1)])
    street_name = models.CharField(max_length=30)
    cost = models.IntegerField(default= 10)
    name = models.CharField(max_length=20, default='parkingLot)
    def __str__(self):
        return str(self.parking_lot_id)


class block(models.Model):
    parking_lot_id = models.ForeignKey(parkingLot, on_delete=models.CASCADE)
    block_id = models.IntegerField(validators=[MinValueValidator(1)])
    is_block_full = models.BooleanField(default=False)
    no_of_floors = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    block_code = models.CharField(max_length=30)
    class Meta:
        unique_together = (('parking_lot_id', 'block_id'),)

    def __str__(self):
        return str(self.block_id)


class floor(models.Model):
    block_id = models.ForeignKey(block, on_delete=models.CASCADE)
    floor_id = models.IntegerField(validators=[MinValueValidator(1)])
    is_floor_full = models.BooleanField(default=False)
    is_covered = models.BooleanField(default=False)
    floor_number = models.IntegerField(validators=[MinValueValidator(1)])
    max_height = models.IntegerField(validators=[MinValueValidator(2)])
    no_of_slots = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    no_of_wings = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    block_code = models.CharField(max_length=30)
    class Meta:
        unique_together = (('block_id', 'floor_id'),)
    def __str__(self):
        return str(self.floor_id)

class parking_slot(models.Model):
    floor_id = models.ForeignKey(floor, on_delete=models.CASCADE)
    parking_slot_id = models.IntegerField(validators=[MinValueValidator(1)])
    wing_code = models.CharField(max_length=10)
    slot_no = models.IntegerField(default=1)
    is_reserved=models.BooleanField(default=False)
    height = models.FloatField(default = 3)
    class Meta:
        unique_together = (('floor_id', 'parking_slot_id'),)
    def __str__(self):
        return str(self.parking_slot_id )
