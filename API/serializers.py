from rest_framework import serializers

from toll.models import Car, Owner, Road, Toll, TollStaion, Traffic


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"


class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = "__all__"


class TollStaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TollStaion
        fields = "__all__"


class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = "__all__"


class TollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toll
        fields = ["car", "toll_station", "date"]
