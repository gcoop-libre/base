# -*- encoding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
from flask import Flask, request, render_template

from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin

# The socket.io namespace
class ChatNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    def on_nickname(self, nickname):
        self.environ.setdefault('nicknames', []).append(nickname)
        self.socket.session['nickname'] = nickname
        self.broadcast_event('announcement', '%s has connected' % nickname)
        self.broadcast_event('nicknames', self.environ['nicknames'])
        # Just have them join a default-named room
        self.join('main_room')

    def on_user_message(self, msg):
        self.emit_to_room('main_room', 'msg_to_room', self.socket.session['nickname'], msg)

    def recv_message(self, message):
        print "PING!!!", message


# Flask routes
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': ChatNamespace})


if __name__ == '__main__':
    print "Este archivo solo contiene el objeto de aplicación"
    print "Intenta con 'python server.py'"

