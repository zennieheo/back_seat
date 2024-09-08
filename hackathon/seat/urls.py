from django.urls import path
from .views import BusListView, SeatUpdateView, websocket_test_view

urlpatterns = [
    path('buses/', BusListView.as_view(), name='bus-list'),
    path('buses/<str:bus_number>/seats/<int:seat_number>/', SeatUpdateView.as_view(), name='seat-update'),

    path('websocket-test/', websocket_test_view, name='websocket_test'),
]
