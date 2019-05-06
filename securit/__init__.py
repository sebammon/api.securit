import os
from flask import Flask
from flask_jwt_extended import JWTManager
from securit import config
from securit.system import System
from flask_pymongo import PyMongo

config = config.DevelopmentConfig
system = System()

app = Flask(__name__)
app.config.from_object(config)

jwt = JWTManager(app)
mongo = PyMongo(app)

# Delayed imports - circular
from securit.views import *
from securit.sensors import initialise_sensors

initialise_sensors()
