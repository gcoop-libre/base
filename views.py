from app import app

from flask import request
from flask import render_template
from flask import send_from_directory
from flask import redirect
from flask import session

from socketio import socketio_manage
import realtime
import models

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
    archivos = models.Archivo.objects
    nombre = session.get('nombre', 'anonimo')
    return render_template('archivos.html', nombre=nombre, archivos=archivos)

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
            usuario = session.get('nombre', 'anonimo')
            models.Archivo.create_by_upload(file, usuario)
            return redirect('/archivos')

    return "hey!"

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': realtime.EventosNamespace})
