from flask import Flask, jsonify, request
from securit import config
from securit.system import Alarm, Statuses

app = Flask(__name__)
config = config.DevelopmentConfig if app.config['ENV'] == 'development' else config.ProductionConfig
app.config.from_object(config)

alarm = Alarm()

# Delayed imports - circular
from securit.sensors import initialise_sensors

initialise_sensors()

@app.route('/')
def server_running():
    return 'Server is running'

@app.route('/alarm/status', methods=['GET'])
def get_alarm_status():
    status = alarm.get_status()
    return jsonify({'status': status})

@app.route('/alarm/status', methods=['POST'])
def set_alarm_status():
    status = request.form.get('status')

    if status is not None:
        new_status = status.upper()
        if new_status in [status.name for status in Statuses]:
            alarm.set_status(status)
            return jsonify({'status': new_status})
            
    return jsonify({'message': 'Please provide a valid status.'})
