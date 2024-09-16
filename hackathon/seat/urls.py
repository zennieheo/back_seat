# seat/ urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeatViewSet, BusViewSet, StopViewSet, SeatListCreateView

router = DefaultRouter()
router.register(r'seats', SeatViewSet)
router.register(r'buses', BusViewSet)
router.register(r'stops', StopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

