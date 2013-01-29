# -*- encoding: utf-8 -*-
import os

from gevent import monkey
monkey.patch_all()

from flask import Flask, request, render_template, send_from_directory, redirect, session
from werkzeug import secure_filename

from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

class EventosNamespace(BaseNamespace, BroadcastMixin):

    def on_enviar_mensaje(self, usuario, mensaje):
        print "Ha llegado el mensaje", mensaje
        self.broadcast_event('conversacion', usuario, mensaje)

# Flask routes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session['nombre'] = request.form['nombre']
        return redirect('/home')

@app.route('/home')
def home():
    nombre = session.get('nombre', 'anonimo')
    return render_template('home.html', nombre=nombre)

@app.route('/archivos')
def archivos():
    archivos = os.listdir('uploads')
    return render_template('archivos.html', archivos=archivos)

@app.route('/chat')
def chat():
    nombre = session.get('nombre', 'anonimo')
    return render_template('chat.html', nombre=nombre)

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

@app.route('/descargar/<path:filename>')
def descargar(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

@app.route('/subir_archivo', methods=['GET', 'POST'])
def subir_archivo():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            return redirect('/archivos')

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': EventosNamespace})


if __name__ == '__main__':
    print "Este archivo solo contiene el objeto de aplicación"
    print "Intenta con 'python server.py'"
