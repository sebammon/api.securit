import os
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from securit import config
from securit.system import System, initialise
from flask_pymongo import PyMongo

config = config.DevelopmentConfig
system = System()
initialise()

app = Flask(__name__)
app.config.from_object(config)

jwt = JWTManager(app)
mongo = PyMongo(app)

# Delayed import for views
from securit.views import *