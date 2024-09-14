# seat/tasks.py
from celery import shared_task
import requests
from .models import BusStop, BusRoute

@shared_task
def update_bus_data():
    # 공공데이터 API 호출
    response = requests.get("API_URL")
    data = response.json()
    
    # 받은 데이터를 이용해 DB에 저장
    for stop_data in data['stops']:
        BusStop.objects.update_or_create(
            stop_id=stop_data['id'],
            defaults={
                'name': stop_data['name'],
                'latitude': stop_data['lat'],
                'longitude': stop_data['lng']
            }
        )
