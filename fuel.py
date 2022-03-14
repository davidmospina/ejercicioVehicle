from engine import *
class fuel:
    def __init__(self,pEngine):
        self.level=1000
        self.engine= pEngine

    def update(self):
        self.level = self.level -abs(self.engine.get_speed())*0.01

        return self.level
    def __str__(self):
        status = "el nivel de fuel es: " + str(self.level)
        return status