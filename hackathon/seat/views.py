# seat/views.py
from rest_framework import viewsets,generics
from rest_framework import viewsets
from .models import Seat, Bus, BusStop
from .serializers import SeatSerializer, BusSerializer, StopSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    @action(detail=False, methods=['get'])
    def by_stop(self, request, stop_id=None):
        # 정류장 가져오기
        stop = BusStop.objects.get(id=stop_id)
        # 해당 정류장을 지나는 모든 버스 가져오기
        buses = stop.buses.all(buses, many=True)  
        serializer = self.get_serializer(buses, many=True)
        return Response(serializer.data)

class StopViewSet(viewsets.ModelViewSet):
    queryset = BusStop.objects.all()
    serializer_class = StopSerializer




# added!
class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
