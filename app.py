# -*- encoding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

from flask import Flask, request, render_template

from socketio import socketio_manage
from socketio.namespace import BaseNamespace
import envoy

class TerminalNamespace(BaseNamespace):

    def on_execute_command(self, command):
        print "Ha llegado el comando", command
        r = envoy.run(command)
        self.emit('result', r.std_out)

    def recv_message(self, message):
        print "PING!!!", message

# Flask routes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/archivos')
def archivos():
    import os
    archivos = os.listdir('uploads')
    return render_template('archivos.html', archivos=archivos)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': TerminalNamespace})

if __name__ == '__main__':
    print "Este archivo solo contiene el objeto de aplicación"
    print "Intenta con 'python server.py'"
