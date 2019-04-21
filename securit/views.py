from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from securit import app

@app.route('/')
def server_running():
    return 'Server is running'

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return jsonify({'message': 'No username or password provided'}), 400

    if username == 'test' and password == 'test':
        auth_token = create_access_token(username)
        return jsonify({'auth_token': auth_token})

    return jsonify({'message': 'Invalid username or password'}), 403

@app.route('/logout')
def logout():
    return 'Logout'

# SENSOR STATUSES
@app.route('/sensors/status', methods=['GET'])
@jwt_required
def get_sensors_status():
    return 'List of sensor statuses'

@app.route('/sensors/status/<int:sensor_id>', methods=['GET'])
@jwt_required
def get_sensors_status_by_id(sensor_id):
    return 'Sensor statuses: {}'.format(sensor_id)

# SENSOR CONFIG
@app.route('/sensors/config', methods=['GET'])
@jwt_required
def get_sensors_config():
    return 'List of sensor configs'

@app.route('/sensors/config', methods=['POST'])
@jwt_required
def create_sensors_config():
    return 'Create sensor config'

@app.route('/sensors/config/<int:sensor_id>', methods=['PUT'])
@jwt_required
def update_sensors_config(sensor_id):
    return 'Update sensor {} config'.format(sensor_id)

# ALARM SYSTEM ACTIONS
@app.route('/alarm/status', methods=['GET'])
@jwt_required
def get_alarm_status():
    return 'Armed'

@app.route('/alarm/status', methods=['PUT'])
@jwt_required
def set_alarm_status():
    return 'Alarm Status Changed'