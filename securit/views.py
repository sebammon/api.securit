from flask import request, jsonify, Response
from flask_jwt_extended import create_access_token, jwt_required
from securit import app, mongo, system
from bson.json_util import dumps
from securit.system import Statuses

mimetype = 'application/json'

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
# @jwt_required
def get_sensors_status():
    return 'List of sensor statuses'

@app.route('/sensors/status/<int:sensor_id>', methods=['GET'])
# @jwt_required
def get_sensors_status_by_id(sensor_id):
    return 'Sensor statuses: {}'.format(sensor_id)

# SENSOR CONFIG
@app.route('/sensors/config', methods=['GET'])
# @jwt_required
def get_sensors_config():
    sensors = mongo.db.sensors.find({}, {'_id': False})
    return Response(dumps(sensors), mimetype=mimetype)

@app.route('/sensors/config', methods=['POST'])
# @jwt_required
def create_sensors_config():
    form_data = request.form
    
    gpio = form_data.get('gpio')
    sensor_name = form_data.get('name')
    sensor_type = form_data.get('type')

    if not gpio and not sensor_name and not sensor_type:
        data = {"gpio": gpio, "name": sensor_name, "type": sensor_type}
        config = mongo.db.sensors.insert(data)
        return Response(dumps(config), mimetype=mimetype)

    return jsonify({'message': 'Sensor config data missing'}), 400

# ALARM SYSTEM ACTIONS
@app.route('/alarm/status', methods=['GET'])
# @jwt_required
def get_alarm_status():
    status = system.get_status()
    return jsonify({'status': status})

@app.route('/alarm/status/<string:status>', methods=['POST'])
# @jwt_required
def set_alarm_status(status):
    new_status = status.upper()
    if new_status in [status.name for status in Statuses]:
        system.set_status(status)
        return jsonify({'status': new_status})
    else:
        return jsonify({'message': 'Please provide a valid status.'})
