from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bus, Seat
from .serializers import BusSerializer, SeatSerializer
from django.shortcuts import get_object_or_404, render #added render

class BusListView(APIView):
    def get(self, request):
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data)

class SeatUpdateView(APIView):
    def post(self, request, bus_number, seat_number):
        bus = get_object_or_404(Bus, bus_number=bus_number)
        seat = get_object_or_404(Seat, bus=bus, seat_number=seat_number)

        # 좌석 선택 또는 해제
        seat.is_occupied = not seat.is_occupied
        seat.save()

        serializer = SeatSerializer(seat)
        return Response(serializer.data)
    


def websocket_test_view(request):
    return render(request, 'seat/websocket_test.html')

