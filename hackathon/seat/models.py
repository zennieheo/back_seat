# seat/models.py
from django.db import models

class BusStop(models.Model):
    stop_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__ (self):
        return self.name
    

class Bus(models.Model):
    bus_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    stops = models.ManyToManyField(BusStop, related_name='buses')

    def __str__(self):
        return self.name
    

class Seat(models.Model):
    OCCUPIED = 'occupied'
    AVAILABLE = 'available'
    SEAT_STATUS_CHOICES = [
        (OCCUPIED, 'Occupied'),
        (AVAILABLE, 'Available')
    ]

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=SEAT_STATUS_CHOICES,
        default=AVAILABLE
    )
    def __str__(self):
        return f"Seat {self.seat_number} on Bus {self.bus.name}"