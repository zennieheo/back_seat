from rest_framework import serializers
from .models import Bus, Seat

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_number', 'is_occupied']

class BusSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Bus
        fields = ['bus_number', 'route', 'seats']
