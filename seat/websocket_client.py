import websocket
import threading
import json

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed with code: {close_status_code} and message: {close_msg}")

def on_open(ws):
    print("Connection opened")

    def run():
        seat_update = {
            "seat_id": 1,
            "status": "occupied"  # 좌석 상태는 'available' 또는 'occupied'로 통일
        }
        ws.send(json.dumps(seat_update))

    threading.Thread(target=run).start()

ws = websocket.WebSocketApp("ws://localhost:8000/ws/seats/",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.on_open = on_open
ws.run_forever()