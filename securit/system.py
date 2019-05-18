from enum import Enum

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
        self.status = Statuses[new_status.upper()]
        return self.status

    def is_armed(self):
        return self.status == Statuses.ARM