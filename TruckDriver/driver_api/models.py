from django.db import models

class Truck(models.Model):
    number_plate = models.CharField(max_length=50, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.number_plate

class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    assigned_truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
        return self.name