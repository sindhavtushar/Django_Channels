# apps.chat.consumers

import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Room

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs'].get('room_name')

        if not self.room_name:
            self.close()
            return

        self.room_group_name = f'chat_{self.room_name}'

        self.room, created = Room.objects.get_or_create(name=self.room_name)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # def receive(self, text_data=None, bytes_data=None):
    #     data = json.loads(text_data)
    #     message = data.get('message')

    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # def chat_message(self, event):
    #     self.send(text_data=json.dumps({
    #         'message': event['message']
    #     }))



    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data.get('message')
        sender = data.get('sender', 'Anonymous')

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))