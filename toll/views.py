from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers import (
    CarSerializer,
    OwnerSerializer,
    TollSerializer,
    TrafficSerializer,
)

from .models import Car, Owner, Toll, TollStaion, Traffic


class TollList(APIView):
    def get(self, request):
        toll = Owner.objects.filter(total_toll_paid__gt=1).order_by("-total_toll_paid")
        serializer = OwnerSerializer(toll, many=True)
        return Response(serializer.data)


class NewTollCreate(APIView):
    def post(self, request, format=None):
        serializer = TollSerializer(data=request.data)
        if serializer.is_valid():
            per_cross = get_object_or_404(TollStaion, id=request.data["toll_station"])
            Toll.objects.create(
                car_id=request.data["car"],
                toll_station_id=request.data["toll_station"],
                date=request.data["date"],
                toll_per_cross=per_cross.toll_per_cross,
            )
            car = get_object_or_404(Car, id=request.data["car"])
            car.total_toll += per_cross.toll_per_cross
            car.save()
            owner = get_object_or_404(Owner, id=car.ownerCar.id)
            owner.total_toll_paid += car.total_toll
            owner.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarTollDetail(APIView):
    def get(self, request, pk, start_date, end_date):
        car = Toll.objects.filter(
            Q(car__id=pk) & Q(date__gt=start_date, date__lt=end_date)
        )

        total = 0
        for i in car:
            total += i.toll_per_cross

        serializer = TollSerializer(car, many=True)
        res = {"total": f" total toll is: {total}", "car": serializer.data}
        return Response(res)


class OwnerTollDetail(APIView):
    def get(self, request, pk, start_date, end_date):
        car = Toll.objects.filter(
            Q(car__ownerCar=pk) & Q(date__gt=start_date, date__lt=end_date)
        )

        total = 0
        for i in car:
            total += i.toll_per_cross

        serializer = TollSerializer(car, many=True)
        res = {"total": f" total toll is: {total}", "car": serializer.data}
        return Response(res)
