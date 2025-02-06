from random import randint, uniform
from time import sleep
from os import system
import sys

# milliamps_to_amps = ma/1000 <- Just for reference
# Need Exceptions Added
# Random button

class Ohms:
    # Placing 3's here for debugging
    def __init__(self):
        self.v = 3
        self.r =  3
        self.i = 3
        self.voltage_equation = 3

    def volts(self):
        self.v = randint(1, 12)
        self.r = randint(100, 1000)
        self.i = round(uniform(0.1, 5), 4)
        self.voltage_equation = self.i*self.r
        self.voltage_equation = round(self.voltage_equation)
        print(self.voltage_equation)
        return self.voltage_equation, self.i, self.r, self.v
                 
    def amps(self):
        self.v = randint(1, 12)
        self.r = round(randint(100, 1000), 2)
        self.i = round(uniform(0.1, 5), 4)
        self.amperage_equation = self.v/self.r
        return self.amperage_equation, self.i, self.r, self.v
        

    def res(self):
            self.v = randint(1, 12)
            self.r = randint(100, 1000)
            self.i = round(uniform(0.1, 5), 4)
            self.resistance_equation = self.v/self.i
            return self.resistance_equation, self.i, self.r, self.v
            
           
    def test(self):
        self.v = randint(1, 12)
        self.r = randint(100, 1000)
        self.i = round(uniform(0.1, 5))
        self.voltage_equation = self.i*self.r

content = Ohms().volts()
voltage_equation, amps, resistance, volts = content
print(f'If you have {resistance} ohms and {amps}, you have {voltage_equation}')


#print("\n\n\n\n")
#v = randint(1, 12)
#r = randint(100, 1000)
#i = round(uniform(0.1, 5))
#voltage_equation = i*r
#print(f"If you have {r} resistance and {i} amps, you have {voltage_equation}")
            






