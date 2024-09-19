# seat/views.py
from rest_framework import viewsets,generics
from .models import Seat, Bus, Stop
from .serializers import SeatSerializer, BusSerializer, StopSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# SeatViewSet은 필요에 따라 유지
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

# 특정 버스의 좌석 정보를 가져오는 API
@api_view(['GET'])
def get_seat_data_by_bus(request, bus_id):
    try:
        bus = Bus.objects.get(id=bus_id)
        seats = Seat.objects.filter(bus=bus)
        seat_data = {seat.seat_number: seat.status for seat in seats}
        return Response(seat_data)
    except Bus.DoesNotExist:
        return Response({'error': 'Bus not found'}, status=404)

# StopViewSet은 그대로 유지
class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

# BusViewSet은 특정 정류장을 지나는 버스 목록을 반환하는 API를 유지
class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    @action(detail=False, methods=['get'])
    def by_stop(self, request, stop_id=None):
        try:
            stop = Stop.objects.get(id=stop_id)
            buses = stop.buses.all()
            serializer = self.get_serializer(buses, many=True)
            return Response(serializer.data)
        except Stop.DoesNotExist:
            return Response({'error': 'Stop not found'}, status=404)

# added!
class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer