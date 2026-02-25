from channels.generic.websocket import AsyncWebsocketConsumer
import json

class LiveCalculatorConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'status':"Connected to channel."
        }))

    async def disconnect(self, code):
        print("Websocked disconnected", code)

    async def receive(self, text_data = None, bytes_data = None):
        print(type(text_data))
        data = json.loads(text_data)
        try:
            expression = data['expression']
            result = eval(expression)
        except ArithmeticError as e:
            result = f'Arithmetic error while solving expression, {e}'
        except Exception as e:
            result = f'Error while solving expression, {e}'
        await self.send(text_data=json.dumps({'solution': result}))
        
