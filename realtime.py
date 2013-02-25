from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin


class EventosNamespace(BaseNamespace, BroadcastMixin):

    def on_enviar_mensaje(self, usuario, mensaje):
        self.broadcast_event('conversacion', usuario, mensaje)

    def on_publicar(self, usuario, archivo):
        self.broadcast_event('publicacion', usuario, archivo)
