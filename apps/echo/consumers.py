from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({'status': 'Connected to Channels'}))

    async def disconnect(self, close_code):
        print("WebSocket disconnected", close_code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        print("Received:", data)
        await self.send(text_data=json.dumps({'echoed': data}))
