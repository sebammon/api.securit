from flask import render_template
from . import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sensor')
def sensor_status():
    return render_template('index.html')