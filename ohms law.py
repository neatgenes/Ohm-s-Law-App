from random import randint, uniform
from time import sleep

# milliamps_to_amps = ma/1000 <- Just for reference

class Ohms:
    def __init__(self):
    #    self.v = randint(1, 12)
    #    self.r = randint(100, 1000)
    #    self.i = round(uniform(0.1, 5), 2)
    #    self.voltage_equation = self.i*self.r
    #    self.amperage_equation = self.v/self.r
    #    self.resistance_equation = self.v/self.i
        self.running = True

    def volts(self):
        while self.running:
            self.v = randint(1, 12)
            self.r = randint(100, 1000)
            self.i = round(uniform(0.1, 5))
            self.voltage_equation = self.i*self.r
            print(f'You have {self.i:.2f} amps and {self.r} resistance')
            sleep(1.5)
            print('How many volts does this mean you have?')
            sleep(1.5)
            print('\nREMEMBER: No matter if your answer is a decimal or not, please add two decimal points.\nThey can be zero')
            answer = input()
            if answer == "{:.2f}".format(self.voltage_equation):
                sleep(1.5)
                print("Correct! The answer is indeed ","{:.2f}".format(self.voltage_equation))    
                sleep(1.5) 
            else: 
                sleep(1.5)
                print('Sorry, that answer is incorrect\nthe correct answer is', "{:.2f}".format(self.voltage_equation) + "\n")
                sleep(1.5)
        
    def amps(self):
        while self.running:
            self.v = randint(1, 12)
            self.r = round(randint(100, 1000), 2)
            self.i = uniform(0.1, 5)
            self.amperage_equation = self.v/self.r
            print(f'You have {self.v} volts and {self.r} resistance')
            sleep(1.5)
            print('How much amperage/current does this mean you have?')
            sleep(1.5)
            print('\nREMEMBER: No matter if your answer is a decimal or not, please add four decimal points.\nThey can be zero')
            answer = input()
            if answer == "{:.4f}".format(self.amperage_equation):
                sleep(1.5)
                print("Correct! The answer is indeed ","{:.4f}".format(self.amperage_equation))    
                sleep(1.5) 
            else: 
                sleep(1.5)
                print('Sorry, that answer is incorrect\nthe correct answer is', "{:.4f}".format(self.amperage_equation) + "\n")
                sleep(1.5)

    def res(self):
        while self.running:
            self.v = randint(1, 12)
            self.r = randint(100, 1000)
            self.i = round(uniform(0.1, 5), 4)
            self.resistance_equation = self.v/self.i
            print(f'You have {self.v} volts and {self.i:.2f} amperage/current')
            sleep(1.5)
            print('How much resistance does this mean you have?')
            sleep(1.5)
            print('\nREMEMBER: No matter if your answer is a decimal or not, please add two decimal points.\nThey can be zero')
            answer = input()
            self.resistance_equation = round(self.resistance_equation, 2)
            if answer == "{:.2f}".format(self.resistance_equation):
                sleep(1.5)
                print("Correct! The answer is indeed ","{:.2f}".format(self.resistance_equation))    
                sleep(1.5) 
            else: 
                sleep(1.5)
                print('Sorry, that answer is incorrect\nthe correct answer is', "{:.2f}".format(self.resistance_equation) + "\n")
                sleep(1.5)

print("Which calculation quiz would you like to take\na) Volts\nb) Amperes)\nc) Reistance)")
answer = input()
match answer:
    case 'a':
        Ohms().volts()
    case 'b':
        Ohms().amps()
    case 'c':
        Ohms().res()
    case _:
        print('invalid option')






