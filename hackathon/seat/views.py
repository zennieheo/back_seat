# seat/views.py
from rest_framework import viewsets
from .models import Seat, BusRoute, BusStop
from .serializers import SeatSerializer, BusRouteSerializer, BusStopSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer

    @action(detail=False, methods=['get'])
    def by_stop(self, request, stop_id=None):
        stop = BusStop.objects.get(id=stop_id)
        buses = stop.routes.all()  # 해당 정류장을 지나는 버스들
        serializer = self.get_serializer(buses, many=True)
        return Response(serializer.data)

class StopViewSet(viewsets.ModelViewSet):
    queryset = BusStop.objects.all()
    serializer_class = BusStopSerializer
