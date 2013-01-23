remote-terminal
===============

Un terminal tipo unix que se puede manejar directamente desde el navegador, 
usando flask, socket.io y angularjs


¿Por qué?
---------

Este repositorio es una prueba de concepto, es inseguro y poco confiable. Lo
realizamos para aprender y poner a prueba unas ideas locas.


Agradecimientos
---------------

Usamos el código inicial que escribió [kcarnold](https://github.com/kcarnold), 
[flask-gevent-socketio-chat](https://github.com/kcarnold/flask-gevent-socketio-chat), para
tener un código inicial de integración con socketio y flask.

Un buen comienzo para investigar es la biblioteca de [Alexandre Bourget](https://github.com/abourget) y su biblioteca [gevent-socketio](https://github.com/abourget/gevent-socketio).

También hay una presentación muy buena de Bourget en Youtube donde muestra
algunos conceptos:

http://youtu.be/zhh_N5pmHBY?t=24m52s

Cómo instalarlo
----------------

Es aconsejable comenzar con un entorno virtual, algo así:

    mkvirtualenv remote-terminal
    pip install -r requirements.txt
    python server.py

Luego ingresa en la aplicación en http://localhost:8080
