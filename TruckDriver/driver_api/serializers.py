from rest_framework import serializers 
from .models import Driver
from .models import Truck
 
 
class DriverSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Driver
        fields = ('id',
                  'name',
                  'mobile_number',
                  'email',
                  'city',
                  'district',
                  'language',
                  'assigned_truck')

class TruckSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Truck
        fields = ('id',
                  'number_plate',
                  'registration_number')