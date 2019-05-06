from securit import system
from securit.system import Statuses
import importlib.util

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

PIR_SENSOR = 4
LED = 17

def check_motion(channel):
    print('Motion detected on channel {}'.format(channel))
    if system.status == Statuses.ARM:
        if not system.triggered:
            system.triggered = True
            print('Alarm triggered by {}!'.format(channel))
            GPIO.output(LED, True)
        else:
            print('Alarm already triggered!')
            pass

def initialise_sensors():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.add_event_detect(PIR_SENSOR, GPIO.RISING, callback=check_motion)