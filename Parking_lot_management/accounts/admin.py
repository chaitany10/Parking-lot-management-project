from django.contrib import admin

from .models import Customer, Regular_Customer, Vehicle_Numbers, Cost


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','firstname', 'lastname', 'phone')


@admin.register(Regular_Customer)
class Regular_CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'purchase_date', 'start_date', 'pass_cost')


@admin.register(Vehicle_Numbers)
class Vehicle_Admin(admin.ModelAdmin):
    list_display = ('customer_id', 'vehicle_no')

@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('cost', 'duration')

