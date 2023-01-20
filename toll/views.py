from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q



from . models import Car , Owner , Road , TollStaion
from . serializers import CarSerializer, OwnerSerializer, RoadSerializer, TollStaionSerializer


class carList (APIView):
    def get (self,request):
        cars = Car.objects.all()
        serializer = CarSerializer (cars, many = True)
        return Response (serializer.data) 
    
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
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