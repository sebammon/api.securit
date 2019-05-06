from enum import Enum

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
