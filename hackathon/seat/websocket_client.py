import websocket
import threading
import json  # JSON 메시지를 보내기 위해 추가

# WebSocket 서버로부터 메시지를 받을 때 호출되는 함수
def on_message(ws, message):
    print(f"Received message: {message}")

# WebSocket 연결에 에러가 발생할 때 호출되는 함수
def on_error(ws, error):
    print(f"Error: {error}")

# WebSocket 연결이 종료될 때 호출되는 함수
def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed with code: {close_status_code} and message: {close_msg}")

# WebSocket 연결이 열리면 호출되는 함수
def on_open(ws):
    print("Connection opened")

    # 서버에 좌석 상태 업데이트 메시지 보내기
    def run():
        seat_update = {
            "seat_id": 1,  # 좌석 ID
            "status": "occupied"  # 좌석 상태 ('available' 또는 'occupied')
        }
        ws.send(json.dumps(seat_update))  # JSON 형식으로 메시지 전송

    # 새로운 스레드에서 메시지를 보내기 위해 스레드 실행
    threading.Thread(target=run).start()

# WebSocketApp 생성
ws = websocket.WebSocketApp("ws://localhost:8000/ws/seats/",  # WebSocket URL 설정
                            on_message=on_message,  # 메시지 수신 시 실행되는 함수
                            on_error=on_error,  # 에러 발생 시 실행되는 함수
                            on_close=on_close)  # 연결 종료 시 실행되는 함수

# WebSocket 연결 열리면 on_open 함수 실행
ws.on_open = on_open

# WebSocket 연결 유지
ws.run_forever()
