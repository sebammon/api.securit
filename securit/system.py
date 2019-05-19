import threading
from enum import Enum


class Statuses(Enum):
    DISARMED = 0
    ARMED = 1
    STAY = 2

class Alarm:
    def __init__(self):
        self.status = Statuses.DISARMED
        self.triggered = False
        self.triggered_thread = None

    def get_status(self):
        return self.status.name
    
    def set_status(self, status):
        from securit.sensors import set_armed_status

        self.status = Statuses[status.upper()]
        if self.status == Statuses.ARMED or self.status == Statuses.STAY:
            set_armed_status(True)
        elif self.status == Statuses.DISARMED:
            set_armed_status(False)
            self.stop()
        return self.status

    def is_armed(self):
        return self.status == Statuses.ARMED

    def is_stay(self):
        return self.status == Statuses.STAY

    def trigger_alarm(self):
        if self.triggered_thread is None:
            self.triggered = True
            self.triggered_thread = threading.Thread(target=self.start)
            self.triggered_thread.start()
            print('Alarm triggered!')

    def stop(self):
        if self.triggered_thread is not None and self.triggered_thread.is_alive():
            self.triggered = False
            self.triggered_thread = None

    def start(self):
        from securit.sensors import blink_alarm_led

        while self.triggered:
            blink_alarm_led()