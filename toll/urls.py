from django.urls import path 
from toll import views


urlpatterns = [
    path ('new-car', views.carList.as_view(), name='car-list'),
    path ('new-owner', views.OwnerList.as_view(), name='owner-list'),
    path ('color-car', views.ColorCarList.as_view(), name='color-car'),
    path ('more-70', views.MoreThan70yearsCarList.as_view(), name='more-70'),
    path ('toll-list', views.TollList.as_view(), name='toll-list'),
    path ('traffic-list', views.TrafficList.as_view(), name='traffic-list'),
]

