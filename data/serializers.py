from rest_framework import serializers
from .models import Country, Car, Parts

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = '__all__'

