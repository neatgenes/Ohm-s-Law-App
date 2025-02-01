from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.uix.label import Label
import kivy.uix
from ohms_law import Ohms
from time import sleep
import asynckivy as ak
from kivy.clock import Clock


# Need To add asynckivy for user input


class Main(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_setup()
        # upon widget size change, update_text_size is called
        self.bind(size=self.update_text_size)
        self.main_text.bind(on_text_validate=self.update_text)
        

    def menu_setup(self):
        self.main_text = TextInput(size=(self.width, self.height*.15), multiline=False)
        self.b1 = Button()
        self.b2 = Button()
        self.l1 = Label(text=('TEST TEST TEST'))
        self.add_widget(self.l1)
        self.add_widget(self.main_text)
        self.add_widget(self.b1)
        self.add_widget(self.b2)
        

    def update_text_size(self, *args):
        self.main_text.size = (self.width, self.height*.15)
        self.b1.pos = (self.center_x, self.height*.15)
        self.b1.size = (self.width/2, self.height*.10)
        self.b2.pos = (0, self.height*.15)
        self.b2.size = (self.width/2, self.height*.10)
        self.l1.pos = (self.center_x-(self.l1.width/2), self.center_y+(self.l1.width/2))
        self.l1.font_size = self.center_x/10



    def update_text(self, *args):
        match self.main_text.text:
            case 'Voltage':
                Ohms().test()
            case 'Amps':
                Ohms().volts()
            case 'Resistance':
                Ohms().volts()
            case 'debug':
                self.main_text.text = "" 
                self.l1.text = f'You have {Ohms().i:.2f} amps and {Ohms().r} resistance\n\n How many volts do you have?'
                if self.main_text.text == "":
                    Clock.schedule_once(self.update_text, 1)
                    self.l1.text = "Sorry, that's incorrect"
                elif self.main_text.text == Ohms().voltage_equation:
                    self.l1.text = 'Great Job!'
                else:
                    self.l1.text = "Sorry, that's incorrect"
                
    
    


                
                




#if answer == "{:.2f}".format(self.voltage_equation):
#                sleep(1.5)
#                print("Correct! The answer is indeed ","{:.2f}".format(self.voltage_equation))    
#                print('Press any button to continue or type "exit" to leave the program')


                

class OhmsLawApp(App):
    pass

OhmsLawApp().run()