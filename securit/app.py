from flask import Flask, jsonify, request
from securit import config
from securit.system import Alarm, Statuses
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
config = config.DevelopmentConfig if app.config.get(
    'ENV') == 'development' else config.ProductionConfig
app.config.from_object(config)

alarm = Alarm()

# Delayed imports - circular
from securit.sensors import initialise_sensors

initialise_sensors()


@api.route('/server')
class Server(Resource):
    def get(self):
        return 'Server is running'


@api.route('/alarm/status')
class AlarmStatus(Resource):
    def get(self):
        status = alarm.get_status()
        return jsonify({'status': status})

    def post(self):
        status = request.form.get('status')

        if status is not None:
            new_status = status.upper()
            if new_status in [status.name for status in Statuses]:
                alarm.set_status(status)
                return jsonify({'status': new_status})

        return jsonify({'message': 'Please provide a valid status.'})
