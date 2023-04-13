from django.http import HttpResponse
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


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_fields = {
        "color": ["exact"],
        "type": ["exact"],
        "ownerCar": ["exact"],
        "ownerCar__age": ["gt"],
    }

    def create(self, request, format=None):
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
