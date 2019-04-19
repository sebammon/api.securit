from flask import render_template, request, jsonify
from securit import app

@app.route('/')
def server_running():
    return 'Server is running'

@app.route('/login')
def login():
    return 'Login Please'

@app.route('/logout')
def logout():
    return 'Logout'

# SENSOR STATUSES
@app.route('/sensors/status', methods=['GET'])
def get_sensors_status():
    print('Query paramters', request.args)
    return 'List of sensor statuses'

@app.route('/sensors/status/<int:sensor_id>', methods=['GET'])
def get_sensors_status_by_id(sensor_id):
    return 'Sensor statuses: {}'.format(sensor_id)

# SENSOR CONFIG
@app.route('/sensors/config', methods=['GET'])
def get_sensors_config():
    return 'List of sensor configs'

@app.route('/sensors/config', methods=['POST'])
def create_sensors_config():
    return 'Create sensor config'

@app.route('/sensors/config/<int:sensor_id>', methods=['PUT'])
def update_sensors_config(sensor_id):
    return 'Update sensor {} config'.format(sensor_id)

# ALARM SYSTEM ACTIONS
@app.route('/alarm/status', methods=['GET'])
def get_alarm_status():
    return 'Armed'

@app.route('/alarm/status', methods=['PUT'])
def set_alarm_status():
    return 'Alarm Status Changed'