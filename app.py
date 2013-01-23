# -*- encoding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
from flask import Flask, request, render_template

from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
import envoy

class TerminalNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):

    def on_nickname(self, nickname):
        self.environ.setdefault('nicknames', []).append(nickname)
        self.socket.session['nickname'] = nickname
        self.broadcast_event('announcement', '%s has connected' % nickname)
        self.broadcast_event('nicknames', self.environ['nicknames'])
        self.join('main_room')

    def on_user_message(self, msg):
        self.emit_to_room('main_room', 'msg_to_room', self.socket.session['nickname'], msg)

    def on_execute_command(self, command):
        print "Ha llegado el comando", command
        r = envoy.run(command)
        self.broadcast_event('result', r.std_out)

    def recv_message(self, message):
        print "PING!!!", message


# Flask routes
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('terminal.html')

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': TerminalNamespace})

if __name__ == '__main__':
    print "Este archivo solo contiene el objeto de aplicación"
    print "Intenta con 'python server.py'"

