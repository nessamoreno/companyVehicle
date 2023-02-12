from django.db import models

# Create your models here.

class VehicleType(models.Model):
    type = models.CharField(max_length=50)
    price =models.DecimalField(max_digits=12, decimal_places=2)

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=6, null=False, unique=True)
    veh_typ_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

class Employee(models.Model):
    identification = models.IntegerField(max_length=10, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(max_length=4, null=False)

class Client(models.Model):
    identification = models.IntegerField(max_length=10, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    number = models.IntegerField(max_length=10, null=False)
    age = models.IntegerField(max_length=4, null=False)

class Rent(models.Model):
    start_date = models.DateTimeField(auto_now_add=False, blank=True)
    final_date = models.DateTimeField(auto_now_add=False, blank=True)
    cli_id = models.ForeignKey(Client, related_name='cli_id', on_delete=models.CASCADE)
    emp_id = models.ForeignKey(Employee, related_name='emp_id', on_delete=models.CASCADE)
    veh_id = models.ForeignKey(Vehicle, related_name='veh_id', on_delete=models.CASCADE)
    amount_payable = models.FloatField(max_length=10, null=False)