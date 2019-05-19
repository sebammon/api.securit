from flask import current_app
from securit.system import Statuses
from time import sleep
import importlib.util

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

SYSTEM_LED = 17
ALARM_LED = 27
STATUS_LED = 4

SIREN = 21

SENSORS = [
    {'gpio': 12, 'name': 'Main Bedroom', 'stay': True},
    {'gpio': 13, 'name': 'Front Door', 'stay': False},
    {'gpio': 14, 'name': 'Lounge', 'stay': True},
    {'gpio': 15, 'name': 'Garage', 'stay': False},
    {'gpio': 16, 'name': 'Outside', 'stay': False},
        ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SYSTEM_LED, GPIO.OUT, initial=GPIO.HIGH) # Keep system LED on
GPIO.setup(ALARM_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(STATUS_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SIREN, GPIO.OUT, initial=GPIO.LOW)

def find_sensor_name(gpio):
    found = list(filter(lambda sensor: sensor['gpio'] == gpio, SENSORS))
    return found[0]['name']

def trigger_stay(gpio):
    filtered_list = list(map(lambda sensor: sensor['gpio'], 
                        filter(lambda sensor: not sensor['stay'], SENSORS)))
    return gpio in filtered_list

def check_motion(gpio):
    from securit.app import alarm

    sensor_name = find_sensor_name(gpio)
    print('Motion detected: {}'.format(sensor_name))
    if alarm.is_armed():
        if not alarm.triggered:
            alarm.trigger_alarm()

    elif alarm.is_stay():
        if trigger_stay(gpio) and not alarm.triggered:
            alarm.trigger_alarm()

def initialise_sensors():
    for sensor in SENSORS:
        GPIO.setup(sensor['gpio'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(sensor['gpio'], GPIO.RISING, callback=check_motion)

def set_armed_status(state):
    GPIO.output(STATUS_LED, state)
    if current_app.config['ENV'] == 'production':
        GPIO.output(SIREN, True)
        sleep(0.1)
        GPIO.output(SIREN, False)
    return state

def blink_alarm_led():
    GPIO.output(ALARM_LED, True)
    sleep(0.5)
    GPIO.output(ALARM_LED, False)
    sleep(0.5)
