import os
from werkzeug.wsgi import SharedDataMiddleware
from socketio.server import SocketIOServer
from app import app

from flask.ext.bootstrap import Bootstrap
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = False
app.config['SECRET_KEY'] = "AF233B"

if __name__ == '__main__':
    print 'Iniciando el servidor en http://localhost:8000'
    app.debug = True
    app.reload = True

    app = SharedDataMiddleware(app, {
        '/': os.path.join(os.path.dirname(__file__), 'static')
        })

    SocketIOServer(('0.0.0.0', 8000), app,
        resource="socket.io", policy_server=False).serve_forever()
