import os
from flask import Flask, render_template
from securit import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

# Delayed import for views
from securit.views import *