from random import randint, uniform
from time import sleep
from os import system
import sys

# milliamps_to_amps = ma/1000 <- Just for reference
# Need Exceptions Added
# Equation for leds and what resistor you need
# adding capacitors in series and parallel
# voltage and amps for parallel and series circuit
# Add voltage drop
# series/parallel circuit resistance calculations
# Tau time canstat = resistance * capacitance
# Resistance for parallel circuits

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
        return self.voltage_equation, self.i, self.r, self.v
                 
    def amps(self):
        self.v = randint(1, 12)
        self.r = round(randint(100, 1000), 2)
        self.i = round(uniform(0.1, 5), 4)
        self.amperage_equation = self.v/self.r
        return self.amperage_equation, self.i, self.r, self.v
        
    # CHANGED INDENTATION, KEEP AN EYE ON THIS JUST IN CASE
    def res(self):
        self.v = randint(1, 12)
        self.r = randint(100, 1000)
        self.i = round(uniform(0.1, 5), 4)
        self.resistance_equation = self.v/self.i
        self.resistance_equation = self.resistance_equation
        return self.resistance_equation, self.i, self.r, self.v
    
    def leds(self):
         # EXAMPLE:
         # YOU HAVE AND LED THAT REQUIRE 3 VOLTS AND 20mAS, WHAT RESISTANCE SHOULD YOU USE IF YOU HAVE A 12 VOLT BATTERY
        self.led_v = randint(2, 3)
        self.ma = 20
        self.v = randint(1, 12)
        self.led_equation = (self.v - self.led_v) / .020
        self.led_equation = round(self.led_equation)
        return self.led_v, self.ma, self.v, self.led_equation
            
           
    def test(self):
        self.v = randint(1, 12)
        self.r = randint(100, 1000)
        self.i = round(uniform(0.1, 5))
        self.voltage_equation = self.i*self.r




#print("\n\n\n\n")
#v = randint(1, 12)
#r = randint(100, 1000)
#i = round(uniform(0.1, 5))
#voltage_equation = i*r
#print(f"If you have {r} resistance and {i} amps, you have {voltage_equation}")
#led_v, ma, v, le = Ohms().leds()
#print(f"If you have an LED that requires {led_v} volts and {ma} miliAmps using a {v} volt battery to power them, what resistance do you need?")
#input()
#print(le)
            






