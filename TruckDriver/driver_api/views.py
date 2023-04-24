# from django.shortcuts import render
# from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view 
from .models import Driver, Truck
from driver_api.serializers import DriverSerializer, TruckSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters

class DriverFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Driver
        fields = ('name', 'mobile_number', 'email', 'language', 'assigned_truck')

@api_view(['GET', 'POST', 'DELETE'])
def driver_list(request):
    if request.method == 'GET':
        driver = Driver.objects.all()
        name = request.GET.get('name', None)
        mobile_number = request.GET.get('mobile_number', None)
        email = request.GET.get('email', None)
        city = request.GET.get('city', None)
        district = request.GET.get('district', None)
        language = request.GET.get('language', None)
        assigned_truck = request.GET.get('assigned_truck', None)
        if name:
            driver = driver.filter(name__icontains=name)
        if mobile_number is not None:
            driver = driver.filter(mobile_number__icontains=mobile_number)
        if email is not None:
            driver = driver.filter(email__icontains=email)
        if language is not None:
            driver = driver.filter(language__icontains=language)
        if assigned_truck is not None:
            driver = Driver.objects.filter(assigned_truck__number_plate__icontains=assigned_truck)
        
        serializer = DriverSerializer(driver, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DriverSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, pk):
    try: 
        driver = Driver.objects.get(pk=pk)
        if request.method == 'GET': 
            driver_serializer = DriverSerializer(driver) 
            return Response(driver_serializer.data)
        elif request.method == 'PUT': 
            driver_data = JSONParser().parse(request) 
            driver_serializer = DriverSerializer(driver, data=driver_data) 
            if driver_serializer.is_valid(): 
                driver_serializer.save() 
                return Response(driver_serializer.data) 
            return Response(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            driver.delete() 
            return Response({'message': 'Driver was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Driver.DoesNotExist: 
        return Response({'message': 'The driver does not exist'}, status=status.HTTP_404_NOT_FOUND)


#TRUCK section: Not required but used to add trucks in the database without using the admin section

@api_view(['GET', 'POST', 'DELETE'])
def truck_list(request):
    if request.method == 'GET':
        truck = Truck.objects.all()
        number_plate = request.GET.get('number_plate', None)
        registration_number = request.GET.get('registration_number', None)
        if number_plate:
            truck = truck.filter(number_plate__icontains=number_plate)
        if registration_number is not None:
            truck = truck.filter(registration_number__icontains=registration_number)
        
        serializer = TruckSerializer(truck, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TruckSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def truck_detail(request, pk):
    try: 
        truck = Truck.objects.get(pk=pk)
        if request.method == 'GET': 
            truck_serializer = TruckSerializer(truck) 
            return Response(truck_serializer.data)
        elif request.method == 'PUT': 
            truck_data = JSONParser().parse(request) 
            truck_serializer = TruckSerializer(truck, data=truck_data) 
            if truck_serializer.is_valid(): 
                truck_serializer.save() 
                return Response(truck_serializer.data) 
            return Response(truck_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            truck.delete()
            return Response({'message': 'Truck was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Truck.DoesNotExist: 
        return Response({'message': 'The truck does not exist'}, status=status.HTTP_404_NOT_FOUND)