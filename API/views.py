from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from toll.models import Car, Owner, Toll, TollStaion, Traffic

from .serializers import (
    CarSerializer,
    OwnerSerializer,
    TollSerializer,
    TrafficSerializer,
)


class OwnerViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    ordering_fields = ["total_toll_paid"]
    ordering = ["-total_toll_paid"]


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_fields = {
        "color": ["exact"],
        "type": ["exact"],
        "ownerCar": ["exact"],
        "ownerCar__age": ["gt"],
    }

    def create(self, request):
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


class TraficViewSet(ModelViewSet):
    queryset = Traffic.objects.all()
    serializer_class = TrafficSerializer
    filterset_fields = {
        "car__type": ["exact"],
        "road__width": ["lt"],
    }


class TollViewSet(ModelViewSet):
    queryset = Toll.objects.all()
    serializer_class = TollSerializer
    filterset_fields = {
        "car": ["exact"],
        "car__ownerCar": ["exact"],
        "date": ["gte", "lte"],
    }

    def create(self, request):
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
