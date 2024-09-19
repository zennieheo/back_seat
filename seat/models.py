# seat/models.py
from django.db import models

class Stop(models.Model):
    stop_id = models.CharField(max_length=100, unique=True, default="default_stop_id")
    name = models.CharField(max_length=100, default="Unknown Stop")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Bus(models.Model):
    bus_id = models.CharField(max_length=100, default="default_bus_id")
    name = models.CharField(max_length=100, default="Unknown Bus")
    stops = models.ManyToManyField(Stop, related_name='buses')

    def __str__(self):
        return self.name

class Seat(models.Model):
    OCCUPIED = 'occupied'
    AVAILABLE = 'available'
    SEAT_STATUS_CHOICES = [
        (OCCUPIED, 'Occupied'),
        (AVAILABLE, 'Available'),
    ]

    seat_number = models.CharField(max_length=10)
    status = models.CharField(
        max_length=10,
        choices=SEAT_STATUS_CHOICES,
        default=AVAILABLE
    )
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='seats')  # Bus와의 관계 추가

    def __str__(self):
        return f"{self.seat_number} ({self.status})"