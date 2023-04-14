from django.urls import path
from rest_framework import routers

from API import views

router = routers.SimpleRouter()
router.register("car", views.CarViewSet, basename="car"),
router.register("owner", views.OwnerViewSet, basename="owner"),
router.register("trafic", views.TraficViewSet, basename="trafic"),
router.register("toll", views.TollViewSet, basename="toll"),

urlpatterns = router.urls
