import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class AsyncCanvasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "update_users"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        print(f"Received: {text_data}")
        data = json.loads(text_data)
        to_send = {"type": "prep", "path": "path"}
        await self.channel_layer.group_send(self.group_name, to_send)

    async def prep(self, event):
        send_json = json.dumps({"path": "path"})
        await self.send(text_data=send_json)