# seat/serializers.py
from rest_framework import serializers
from .models import Seat, Stop, Bus

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['id', 'name', 'latitude', 'longitude']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'status', 'bus']

class BusSerializer(serializers.ModelSerializer):
    stops = StopSerializer(many=True, read_only=True)

    class Meta:
        model = Bus
        fields = ['id', 'name', 'stops']
