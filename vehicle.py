from blinker import *
from fuel import *
from engine import *
from light import *
from environment import *

class Vehicle:
    def __init__(self):
        self.blinker_front = Blinker(BLINKER_FRONT)
        self.blinker_rear = Blinker(BLINKER_REAR)
        self.engine = engine()
        self.fuel = fuel(self.engine)
        self.environment = environment()
        self.light = light(self.environment)

    def __str__(self):
        status ='front blink: ' + str(self.blinker_front)+ ' ' + 'rear blink: '+ str(self.blinker_rear) + '\n'+ str(self.engine) + '\n' + str(self.environment) + '\n' + str(self.fuel) + '\n' + str(self.light) + '\n' 
        return status


    def do_work(self):

        while True:            
            print(self)

            key = input('next action (q quit): ')
            if key == 's':
                self.blinker_front.change()
                print(self.blinker_front)
            if key == 'a':
                self.blinker_rear.change()
                print(self.blinker_rear)
            if key == 'w':
                self.engine.modify_rpm(100)
                print(self.engine)
            if key == 'z':
                self.engine.modify_rpm(-100)
            if key == 'e':
                self.engine.modify_gear(1)
            if key == 'd':
                self.engine.modify_gear(-1)
            if key == 'r':
                self.environment.modify_lum(10)
            if key == 'f':
                self.environment.modify_lum(-10)

            if key == 'q':
                exit()
            
            self.light.update()
            self.fuel.update()


if __name__ == "__main__":
    vehicle1 = Vehicle()
    vehicle1.do_work()

