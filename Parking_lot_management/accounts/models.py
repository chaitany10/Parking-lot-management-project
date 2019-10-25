from django.db import models


# Create your models here.

class Customer(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )
    customer_id = models.CharField(unique=True, max_length=20)
    firstname = models.CharField(blank=True, max_length=50)
    lastname = models.CharField(blank=True, max_length=50)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    phone = models.CharField(blank=True, max_length=10)

    def get_populated_fields(self):
        """
        To collect form data
        :return:
        """
        fields = {}
        if self.firstname is not None:
            fields['firstname'] = self.firstname
        if self.lastname is not None:
            fields['lastname'] = self.lastname
        if self.sex is not None:
            fields['sex'] = self.sex
        if self.phone is not None:
            fields['phone'] = self.phone

        return fields

    def __str__(self):
        return self.firstname + " " + self.lastname


class Regular_Customer(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now=True)
    start_date = models.DateField(auto_now=True)
    pass_cost = models.IntegerField()


class Vehicle_Numbers(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=20)


class Cost(models.Model):
    cost = models.OneToOneField(Regular_Customer, primary_key=True, on_delete=models.CASCADE)
    duration = models.IntegerField(default=30)
