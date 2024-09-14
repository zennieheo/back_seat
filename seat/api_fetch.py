import requests
from .models import Stop

def fetch_stops():
    API_KEY = '2iuH528tnR8%2FsHcLsonGa95bqI36aAw%2BEewaRWx6FTKWtval6Co5CFL0hEOLGUpclUdwaYoEj9b7WeX7LxKI3Q%3D%3D'
    BASE_URL = 'http://data.seoul.go.kr/dataList/OA-13059/S/1/datasetView.do'  

    try:
        response = requests.get(f"{BASE_URL}?apiKey={API_KEY}")
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        data = response.json()

        for stop in data['stops']:
            Stop.objects.update_or_create(
                stop_name=stop['name'],
                defaults={
                    'latitude': stop['latitude'],
                    'longitude': stop['longitude'],
                }
            )
        print("정류장 정보가 성공적으로 업데이트되었습니다.")
    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 에러가 발생했습니다: {e}")