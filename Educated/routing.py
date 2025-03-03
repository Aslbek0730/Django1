from django.conf.urls import url

from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from Educated.consumers import Educated_WebSocketConsumer

# Consumer Imports
from student.consumers import studentConsumer
from Admin.consumers import AdminConsumer


application = ProtocolTypeRouter({

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^ws/$", Educated_WebSocketConsumer.as_asgi()),
        ])
    ),
    "channel": ChannelNameRouter({
        "student": studentConsumer,    "Admin": AdminConsumer,
    })
})
