from securit.system import Statuses
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

def find_sensor_name(gpio):
    found = list(filter(lambda sensor: sensor['gpio'] == gpio, SENSORS))
    return found[0]['name']

def check_motion(channel):
    from securit import system
    sensor_name = find_sensor_name(channel)
    print('Motion detected by: {}'.format(sensor_name))
    if system.is_armed():
        if not system.triggered:
            system.triggered = True
            print('Alarm triggered!')
        else:
            print('Alarm already triggered!')
            pass

def initialise_sensors():
    for sensor in SENSORS:
        GPIO.setup(sensor['gpio'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(sensor['gpio'], GPIO.RISING, callback=check_motion)

def set_status_led(state):
    GPIO.output(STATUS_LED, state)