from environment import *
class light:
    def __init__(self,pEnvironment):
        self.activated = False
        self.environment = pEnvironment
    def update(self):
        if self.environment.get_lum() <= 40:
            self.activated = True
        else:
            self.activated = False

    def __str__(self):

        status = "Estado de las luces: " + str(self.activated)

        return status
