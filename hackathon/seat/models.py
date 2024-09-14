# seat/models.py
from django.db import models

# 정류장 > 노선 관계는 busstop과 busroute모델에서 ManyToMany 필드로 설정
class BusStop(models.Model):
    stop_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class BusRoute(models.Model):
    route_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    stops = models.ManyToManyField(BusStop, related_name='routes') # stops >routes 관계만 잇음

class Seat(models.Model):
    OCCUPIED = 'occupied'
    AVAILABLE = 'available'
    SEAT_STATUS_CHOICES = [
        (OCCUPIED, 'Occupied'),
        (AVAILABLE, 'Available')
    ]

    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=SEAT_STATUS_CHOICES,
        default=AVAILABLE
    )
