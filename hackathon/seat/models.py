from django.db import models

class Bus(models.Model):
    bus_number = models.CharField(max_length=10)  # 버스 번호
    route = models.TextField()  # 버스 경로 정보 (예: json)

    def __str__(self):
        return self.bus_number

class Seat(models.Model):
    bus = models.ForeignKey(Bus, related_name='seats', on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bus {self.bus.bus_number} - Seat {self.seat_number}"
