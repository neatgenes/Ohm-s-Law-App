from random import randint, uniform
from time import sleep
from os import system
import sys

# milliamps_to_amps = ma/1000 <- Just for reference
# Need Exceptions Added
# Random button
# if you don't add the proper decimals add proper amount of decimals for user
#system('cls')
#print('                    Electronics Calculation Knowledge Quiz')
#sleep(1.2)
#print("                             Developed by JC ")
#sleep(3)
#system('cls')

#started = True

class Ohms:
    def __init__(self):
        self.running = True
        self.v = randint(1, 12)
        self.r = randint(100, 1000)
        self.i = round(uniform(0.1, 5))
        self.voltage_equation = self.i*self.r

    def volts(self):
        while self.running:
            self.v = randint(1, 12)
            self.r = randint(100, 1000)
            self.i = round(uniform(0.1, 5))
            self.voltage_equation = self.i*self.r
            
            print('How many volts does this mean you have?')
            sleep(1.5)
            print('\nREMEMBER: No matter if your answer is a decimal or not, please add two decimal points.\nThey can be zero')
            answer = input()
            if answer == "{:.2f}".format(self.voltage_equation):
                sleep(1.5)
                print("Correct! The answer is indeed ","{:.2f}".format(self.voltage_equation))    
                print('Press any button to continue or type "exit" to leave the program')
                answer = input()
                if answer == 'exit':
                    self.running = False
                sleep(1.5) 
                system('cls')

            else: 
                sleep(1.5)
                print('Sorry, that answer is incorrect\nthe correct answer is', "{:.2f}".format(self.voltage_equation) + "\n")
                print('Press any button to continue or type "exit" to leave the program')
                answer = input()
                if answer == 'exit':
                    self.running = False
                sleep(1.5)
                system('cls')
        
    def amps(self):
        while self.running:
            self.v = randint(1, 12)
            self.r = round(randint(100, 1000), 2)
            self.i = uniform(0.1, 5)
            self.amperage_equation = self.v/self.r
            system('cls')
            print(f'You have {self.v} volts and {self.r} resistance')
            sleep(1.5)
            print('How much amperage/current does this mean you have?')
            sleep(1.5)
            print('\nREMEMBER: No matter if your answer is a decimal or not, please add four decimal points.\nThey can be zero')
            answer = input()
            if answer == "{:.4f}".format(self.amperage_equation):
                sleep(1.5)
                print("Correct! The answer is indeed ","{:.4f}".format(self.amperage_equation))    
                print('Press any button to continue or type "exit" to leave the program')
                answer = input()
                if answer == 'exit':
                    self.running = False

                sleep(1.5) 
                system('cls')
            else: 
                sleep(1.5)
                print('Sorry, that answer is incorrect\nthe correct answer is', "{:.4f}".format(self.amperage_equation) + "\n")
                print('Press any button to continue or type "exit" to leave the program')
                answer = input()
                if answer == 'exit':
                    self.running = False

                sleep(1.5)
                system('cls')

    def res(self):
        while self.running:
            self.v = randint(1, 12)
            self.r = randint(100, 1000)
            self.i = round(uniform(0.1, 5), 4)
            self.resistance_equation = self.v/self.i
            system('cls')
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
                print('Press any button to continue or type "exit" to leave the program')
                answer = input()
                if answer == 'exit':
                    self.running = False

                sleep(1.5) 
                system('cls')
            else: 
                sleep(1.5)
                print('Sorry, that answer is incorrect\nthe correct answer is', "{:.2f}".format(self.resistance_equation) + "\n")
                print('Press any button to continue or type "exit" to leave the program')
                answer = input()
                if answer == 'exit':
                    self.running = False
                sleep(1.5)
                system('cls')
    def test(self):
        self.v = randint(1, 12)
        self.r = randint(100, 1000)
        self.i = round(uniform(0.1, 5))
        self.voltage_equation = self.i*self.r
        

#while started:
#    print("Which calculation quiz would you like to take\na) Volts\nb) Amperes)\nc) Reistance)\nd) Exit")
#    answer = input()
#    match answer:
#        case 'a':
#            Ohms().volts()
#        case 'b':
#            Ohms().amps()
#        case 'c':
#            Ohms().res()
#        case 'd':
#            started = False
#        case _:
#            print('invalid option')
            






