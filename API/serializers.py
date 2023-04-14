from rest_framework import serializers

from toll.models import Car, Owner, Toll, Traffic


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"


class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = "__all__"


class TollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toll
        fields = "__all__"
        read_only_fields = ("toll_per_cross",)
