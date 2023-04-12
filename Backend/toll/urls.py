from django.urls import path

from toll import views

urlpatterns = [
    path("new-car", views.carList.as_view(), name="car-list"),
    path("new-owner", views.OwnerList.as_view(), name="owner-list"),
    path("color-car", views.ColorCarList.as_view(), name="color-car"),
    path("more-70", views.MoreThan70yearsCarList.as_view(), name="more-70"),
    path("toll-list", views.TollList.as_view(), name="toll-list"),
    path("traffic-list", views.TrafficList.as_view(), name="traffic-list"),
    path("new-toll", views.NewTollCreate.as_view(), name="new-toll"),
    path(
        "car-toll-detail/<int:pk>/<str:start_date>/<str:end_date>",
        views.CarTollDetail.as_view(),
        name="car-toll-detail",
    ),
    path(
        "owner-toll-detail/<int:pk>/<str:start_date>/<str:end_date>",
        views.OwnerTollDetail.as_view(),
        name="owner-toll-detail",
    ),
]
