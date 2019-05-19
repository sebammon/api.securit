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
    
    def set_status(self, status):
        from securit.sensors import set_armed

        next_status = Statuses[status.upper()]

        if next_status == Statuses.ARMED:
            set_armed(True)
        elif next_status == Statuses.DISARMED:
            set_armed(False)
            self.triggered = False
        self.status = next_status
        return self.status

    def is_armed(self):
        return self.status == Statuses.ARMED