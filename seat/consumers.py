# seat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Seat
from django.core.exceptions import ObjectDoesNotExist
import redis  # Redis 사용을 위한 import

# Redis 클라이언트 설정 (ElastiCache의 Redis 엔드포인트를 사용)
redis_client = redis.StrictRedis(
    host='your-redis-cluster-endpoint',  # ElastiCache 기본 엔드포인트
    port=6379,
    decode_responses=True
)


class SeatConsumer(AsyncWebsocketConsumer):
    async def connect(self): # 클라이언트가 websocket에 연결될 때 호출된다.
        self.room_group_name = 'seat_updates'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code): # 클라이언트가 연결을 끊을 때 호출됨. 
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data): # 클라이언트가 ㅈebsocket을 통해 메시지를 보낼 때 호출됨. 
        try:
            text_data_json = json.loads(text_data)
            seat_id = text_data_json['seat_id']
            status = text_data_json['status']
            
            # 좌석 상태를 Redis에 업데이트
            await self.update_seat_status_redis(seat_id, status)  # 수정된 부분

            # 그룹에 메시지 브로드캐스트
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'seat_status_update',
                    'seat_id': seat_id,
                    'status': status
                }
            )
        except Exception as e:
            print(f"Error processing message: {e}")
            await self.close()

    @sync_to_async
    def update_seat_status_redis(self, seat_id, status):  # Redis 사용을 위한 좌석 상태 업데이트 (수정된 부분)
        try:
            # Redis에 좌석 상태 저장
            redis_client.set(f'seat:{seat_id}', status)  # Redis에 좌석 상태 저장 (수정된 부분)

            # Django DB에도 좌석 상태 업데이트 (옵션)
            seat = Seat.objects.get(id=seat_id)
            seat.status = status
            seat.save()
        except ObjectDoesNotExist:
            print(f"Seat with id {seat_id} does not exist.")
    
    @sync_to_async
    def get_seat_status_from_redis(self, seat_id):  # Redis에서 좌석 상태를 가져오는 함수 (새로운 함수)
        return redis_client.get(f'seat:{seat_id}')

    async def seat_status_update(self, event):  # 좌석 상태 업데이트 메시지를 보낼 때 호출됨
        await self.send(text_data=json.dumps({
            'seat_id': event['seat_id'],
            'status': event['status']
        }))
