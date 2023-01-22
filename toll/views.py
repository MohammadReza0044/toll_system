from django.http import HttpResponse
from django.shortcuts import get_object_or_404 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


from . models import Car , Owner ,Traffic, Road , TollStaion, Toll 
from . serializers import CarSerializer, OwnerSerializer, TrafficSerializer, TollSerializer


class carList (APIView):
    def get (self,request):
        cars = Car.objects.all()
        serializer = CarSerializer (cars, many = True)
        return Response (serializer.data) 
    
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            if request.data['type'] == 'BIG':
                new_big = Car.objects.filter(ownerCar__id = request.data['ownerCar'] , type = 'BIG')
                if new_big.exists():
                    return HttpResponse ('کاربر نمیتواند دو تا ماشین سنگین داشته باشد')
                else: 
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorCarList (APIView):
    def get (self,request):
        cars = Car.objects.filter(
            Q(color='red') | Q(color='blue') 
        )
        serializer = CarSerializer (cars, many = True)
        return Response (serializer.data) 


class MoreThan70yearsCarList (APIView):
    def get (self,request):
        cars = Car.objects.filter(ownerCar__age__gt= 70)
        serializer = CarSerializer (cars, many = True)
        return Response (serializer.data)



class OwnerList (APIView):
    def get (self,request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer (owners, many = True)
        return Response (serializer.data) 
    
    def post(self, request, format=None):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TollList (APIView):
    def get (self,request):
        toll = Owner.objects.filter(
            total_toll_paid__gt = 1
        ).only('name','national_code').order_by('-total_toll_paid')
        serializer = OwnerSerializer (toll, many = True)
        return Response (serializer.data) 

    
class TrafficList (APIView):
    def get (self,request):
        traffic = Traffic.objects.filter(
            Q(car__type='BIG') & Q(road__width__lt= 20) 
        )
        serializer = TrafficSerializer (traffic, many = True)
        return Response (serializer.data) 


class TollList (APIView):
    def get (self,request,pk):
        toll_list = Toll.objects.filter(car = pk)
        serializer = TollSerializer (toll_list, many = True)
        return Response (serializer.data) 
    
    def post(self, request, format=None):
        serializer = TollSerializer(data=request.data)
        if serializer.is_valid():
            per_cross = get_object_or_404(TollStaion, id = request.data['toll_station'])
            Toll.objects.create(
                car_id = request.data['car'],
                toll_station_id = request.data['toll_station'],
                date = request.data['date'],
                toll_per_cross = per_cross.toll_per_cross
            )
            car = get_object_or_404(Car , id = request.data['car'] )
            car.total_toll += per_cross.toll_per_cross
            car.save()
            owner = get_object_or_404(Owner , id = car.ownerCar.id )
            owner.total_toll_paid += car.total_toll
            owner.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
