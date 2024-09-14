from celery import shared_task
from .api_fetch import fetch_stops

@shared_task
def update_stops():
    fetch_stops()