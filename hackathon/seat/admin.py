from django.contrib import admin
from .models import BusStop, Bus, Seat

@admin.register(BusStop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('stop_id', 'name', 'latitude', 'longitude')
    search_fields = ('name', 'stop_id')

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_id', 'name')
    search_fields = ('name', 'bus_id')
    filter_horizontal = ('stops',)  # ManyToMany 필드의 경우 horizontal filter 추가

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('bus', 'seat_number', 'status')
    list_filter = ('bus', 'status')
    search_fields = ('seat_number', 'bus__name')  # bus name을 통해 검색 가능


