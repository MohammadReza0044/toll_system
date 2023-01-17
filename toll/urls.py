from django.urls import path 

from . views import carList, OwnerList , RoadList, ColorCarList, MoreThan70yearsCarList

urlpatterns = [
    path ('new-car', carList.as_view(), name='car-list'),
    path ('new-owner', OwnerList.as_view(), name='owner-list'),
    path ('color-car', ColorCarList.as_view(), name='color-car'),
    path ('more-70', MoreThan70yearsCarList.as_view(), name='more-70'),
    path ('new-road', RoadList.as_view(), name='road-list'),
]
