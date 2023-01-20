from rest_framework import serializers

from . models import Car , Owner , Road , TollStaion

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
    


class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'


class TollStaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TollStaion
        fields = '__all__'