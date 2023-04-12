from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..API.serializers import (
    CarSerializer,
    OwnerSerializer,
    TollSerializer,
    TrafficSerializer,
)
from .models import Car, Owner, Toll, TollStaion, Traffic


class carList(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            if request.data["type"] == "BIG":
                new_big = Car.objects.filter(
                    ownerCar__id=request.data["ownerCar"], type="BIG"
                )
                if new_big.exists():
                    return HttpResponse("کاربر نمیتواند دو تا ماشین سنگین داشته باشد")
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorCarList(APIView):
    def get(self, request):
        cars = Car.objects.filter(Q(color="red") | Q(color="blue"))
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class MoreThan70yearsCarList(APIView):
    def get(self, request):
        cars = Car.objects.filter(ownerCar__age__gt=70)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class OwnerList(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TollList(APIView):
    def get(self, request):
        toll = Owner.objects.filter(total_toll_paid__gt=1).order_by("-total_toll_paid")
        serializer = OwnerSerializer(toll, many=True)
        return Response(serializer.data)


class TrafficList(APIView):
    def get(self, request):
        traffic = Traffic.objects.filter(Q(car__type="BIG") & Q(road__width__lt=20))
        serializer = TrafficSerializer(traffic, many=True)
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
