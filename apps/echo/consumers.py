import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer
from .helpers import generate_board

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

ROOMS = {}

class BingoConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"bingo_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # generate board
        board = generate_board()

        await self.send(text_data=json.dumps({
            "type": "board",
            "board": board
        }))

        # ALSO send sync state
        if self.room_name not in ROOMS:
            ROOMS[self.room_name] = {
                "drawn_numbers": [],
                "started": False
            }

        await self.send(text_data=json.dumps({
            "type": "sync",
            "drawn_numbers": ROOMS[self.room_name]["drawn_numbers"],
            "started": ROOMS[self.room_name]["started"]
        }))


    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "start":
            ROOMS[self.room_name]["started"] = True

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "game_started"
                }
            )

        elif action == "draw":
            available = list(set(range(1, 76)) - set(ROOMS[self.room_name]["drawn_numbers"]))

            if not available:
                return

            number = random.choice(available)
            ROOMS[self.room_name]["drawn_numbers"].append(number)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "number_drawn",
                    "number": number
                }
            )

    async def number_drawn(self, event):
        await self.send(text_data=json.dumps({
            "type": "number_drawn",
            "number": event["number"]
        }))

    async def game_started(self, event):
        await self.send(text_data=json.dumps({
            "type": "game_started"
        }))