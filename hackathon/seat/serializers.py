# seat/serializers.py
from rest_framework import serializers
from .models import Seat, BusStop, BusRoute

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = ['id', 'name', 'latitude', 'longitude']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'status', 'bus_route']

class BusRouteSerializer(serializers.ModelSerializer):
    stops = BusStopSerializer(many=True, read_only=True)

    class Meta:
        model = BusRoute
        fields = ['id', 'name', 'stops']
