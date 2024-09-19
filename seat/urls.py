# seat/ urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeatViewSet, BusViewSet, StopViewSet, SeatListCreateView, get_seat_data_by_bus

router = DefaultRouter()
router.register(r'seats', SeatViewSet)
router.register(r'buses', BusViewSet)
router.register(r'stops', StopViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/seat/by-bus/<int:bus_id>/', get_seat_data_by_bus),  # 특정 버스의 좌석 정보 API
]