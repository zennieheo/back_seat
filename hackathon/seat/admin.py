from django.contrib import admin
from .models import BusStop, BusRoute, Seat

# Register your models here.
admin.site.register(BusStop)
admin.site.register(BusRoute)
admin.site.register(Seat)
