from datetime import datetime

class Patient:
    def __init__(self, pid, name, age, gender):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender

class Ward:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.occupied = 0

    def assign_bed(self):
        if self.occupied < self.capacity:
            self.occupied += 1
            return True
        return False

    def discharge_bed(self):
        if self.occupied > 0:
            self.occupied -= 1

class Admission:
    def __init__(self, pid, ward):
        self.pid = pid
        self.ward = ward
        self.admit_date = datetime.now()
        self.discharge_date = None

    def discharge(self):
        self.discharge_date = datetime.now()

class Bill:
    def __init__(self, pid, amount):
        self.pid = pid
        self.amount = amount