import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bus_number = self.scope['url_route']['kwargs']['bus_number']
        self.room_group_name = f'bus_{self.bus_number}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        seat_number = data['seat_number']
        is_occupied = data['is_occupied']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'seat_update',
                'seat_number': seat_number,
                'is_occupied': is_occupied
            }
        )

    async def seat_update(self, event):
        await self.send(text_data=json.dumps({
            'seat_number': event['seat_number'],
            'is_occupied': event['is_occupied']
        }))







# added for testing!

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'WebSocket connected!'
        }))

    async def disconnect(self, close_code):
        print('WebSocket disconnected:', close_code)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Echo the received message back to the client
        await self.send(text_data=json.dumps({
            'message': message
        }))