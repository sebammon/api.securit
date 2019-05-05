from enum import Enum
from securit import system
import importlib.util

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

PIR_SENSOR = 4
LED = 17

def check_motion(channel):
    print('Motion was detected on channel {}'.format(channel))

    if system.status == Status.ARM:
        print('Trigger alarm')
        GPIO.output(LED, True)

def initialise():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PIR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(LED, GPIO.OUT)

    GPIO.add_event_detect(PIR_SENSOR, GPIO.RISING, callback=check_motion)

    print('LED', LED)

class Status(Enum):
    DISARM = 0
    ARM = 1
    STAY = 2

class System:
    def __init__(self):
        self.status = Status.DISARM

    def get_status(self):
        return self.status.name
    
    def set_status(self, new_status: str):
        self.status = Status[new_status.upper()]
        return self.status