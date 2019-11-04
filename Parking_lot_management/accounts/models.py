from django.db import models


# Create your models here.

class Customer(models.Model):

    customer_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(blank=True, max_length=50)
    lastname = models.CharField(blank=True, max_length=50)

    phone = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.customer_id


class Regular_Customer(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now=True)
    start_date = models.DateField(auto_now=True)
    pass_cost = models.IntegerField()


class Vehicle_Numbers(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=20)
    vehicle_height = models.FloatField(default=1.5)


class Cost(models.Model):
    cost = models.OneToOneField(Regular_Customer, primary_key=True, on_delete=models.CASCADE)
    duration = models.IntegerField(default=30)
