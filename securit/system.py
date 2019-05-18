from enum import Enum
from securit.sensors import set_status_led

class Statuses(Enum):
    DISARM = 0
    ARM = 1
    STAY = 2

class System:
    def __init__(self):
        self.status = Statuses.DISARM
        self.triggered = False

    def get_status(self):
        return self.status.name
    
    def set_status(self, new_status: str):
        next_status = Statuses[new_status.upper()]
        if new_status == Statuses.ARM:
            set_status_led(True)
        elif new_status == Statuses.DISARM:
            set_status_led(False)
            self.triggered = False
        self.status = next_status
        return self.status

    def is_armed(self):
        return self.status == Statuses.ARM