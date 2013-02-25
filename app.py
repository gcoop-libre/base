# -*- encoding: utf-8 -*-
from flask import Flask

# Flask routes
app = Flask(__name__)

# Base de datos
from flask.ext.mongoengine import MongoEngine
app.config['MONGODB_SETTINGS'] = {'DB': 'base'}
db = MongoEngine(app)

if __name__ == '__main__':
    print "Este archivo solo contiene el objeto de aplicación"
    print "Intenta con 'python server.py'"
