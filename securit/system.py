from enum import Enum

class Statuses(Enum):
    DISARMED = 0
    ARMED = 1
    STAY = 2

class Alarm:
    def __init__(self):
        self.status = Statuses.DISARMED
        self.triggered = False

    def get_status(self):
        return self.status.name
    
    def set_status(self, new_status):
        from securit.sensors import set_status_led
        next_status = Statuses[new_status.upper()]
        if new_status == Statuses.ARMED:
            set_status_led(True)
        elif new_status == Statuses.DISARMED:
            set_status_led(False)
            self.triggered = False
        self.status = next_status
        return self.status

    def is_armed(self):
        return self.status == Statuses.ARMED