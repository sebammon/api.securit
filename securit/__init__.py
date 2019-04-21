import os
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from securit import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

jwt = JWTManager(app)

# Delayed import for views
from securit.views import *