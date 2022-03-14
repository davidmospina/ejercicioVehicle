speed = 0
class engine:
    def __init__(self):
        self.rpm = 0
        self.gear = 0

    def modify_rpm(self,prpm):
        self.rpm = prpm

    def modify_gear(self,pgear):
        self.gear = pgear

    def get_speed(self):
        if self.gear >= 0
            speed = (self.rpm*self.gear/5)/10
        elif self.rpm>0:
            speed = -10
        else:
            speed = 0

    def __str__(self):
        status = "rpm:" + str(self.rpm) + " gear: " + str(self.gear) + " velocity: " + str(speed)
        return status

