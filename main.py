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

# TODAY GET THE ALGORITHMS WORKING
# Add two decimal spaces if user doesn't add them. We might want to add 4 decimal places for amps

# Need To add asynckivy for user input
# Add voltage drop
# Tau time canstat = resistance * capacitance
# Resistance for parallel circuits
class Main(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_setup()
        # upon widget size change, update_text_size is called
        self.bind(size=self.update_text_size)
        #self.main_text.bind(on_text_validate=self.update_text)
        self.volts_button.bind(on_press=self.volts_udpate)
        self.amps_button.bind(on_press=self.amps_udpate)
        self.res_button.bind(on_press=self.res_udpate)
        

    def menu_setup(self):
        self.main_text = TextInput(size=(self.width, self.height*.15), multiline=False)
        self.volts_button = Button(text='Voltage Questions')
        self.amps_button = Button(text='Amperage Questions')
        self.res_button = Button(text='Resistance Questions')
        self.l1 = Label(text=("Ohm's Law Calculation Test"))
        self.add_widget(self.l1)
        self.add_widget(self.main_text)
        self.add_widget(self.volts_button)
        self.add_widget(self.amps_button)
        self.add_widget(self.res_button)
        
# 
    def update_text_size(self, *args):
        self.main_text.size = (self.width, self.height*.15)
        self.volts_button.pos = (0, self.height*.15)
        self.volts_button.size = (self.width/3, self.height*.10)
        self.amps_button.pos = (self.volts_button.width, self.height*.15)
        self.amps_button.size = (self.width/3, self.height*.10)
        self.res_button.pos = (self.volts_button.width*2, self.height*.15)
        self.res_button.size = (self.width/3, self.height*.10)
        self.l1.pos = (self.center_x-(self.l1.width/2), self.center_y+(self.l1.width/2))
        self.l1.font_size = self.center_x/10
        
    def volts_udpate(self, *args):
        Ohms().volts()
        self.running = True
        ak.start(self.voltage())

    def amps_udpate(self, *args):
        Ohms().amps()
        self.running = True
        ak.start(self.amperage())

    def res_udpate(self, *args):
        Ohms().res()
        self.running = True
        ak.start(self.resistance())
    
    async def voltage(self):
        print('voltage')
        content = Ohms().volts()
        voltage_equation, amps, resistance, volts = content

        def update_label_text(text):
            self.l1.text = text

        #self.main_text.bind(on_text_validate=self.update_text)
        self.main_text.text = "" 
        self.l1.text = f'You have {amps:.2f} amps and {resistance} resistance\n\n How many volts do you have?'
        
        await ak.event(self.main_text, 'on_text_validate')
        print(voltage_equation)

        
        if self.main_text.text == str(voltage_equation):
            Clock.schedule_once(lambda dt: update_label_text('Great Job!'))
            print('if is working')
            
    
        else:
            Clock.schedule_once(lambda dt: update_label_text("Sorry, that's incorrect"))
            print('else is working')
            
    
    # AMPS HERE
    # NEED TO ROUND THE NUMBERS AND FIGURE OUT HOW TO SEND RES AS FLOAT
    async def amperage(self):
        print('amps')
        content = Ohms().amps()
        amps_equation, amps, resistance, volts = content

        def update_label_text(text):
            self.l1.text = text

        self.main_text.text = "" 
        self.l1.text = f'You have {volts} volts and {resistance} resistance\n\n How many amps do you have?'
        
        await ak.event(self.main_text, 'on_text_validate')
        print(f"{amps_equation:.2f}")

        if self.main_text.text == str(f"{amps_equation:.2f}"):
            Clock.schedule_once(lambda dt: update_label_text('Great Job!'))
            print('if is working')
            
    
        else:
            Clock.schedule_once(lambda dt: update_label_text("Sorry, that's incorrect"))
            print('else is working')
          

    # RESISTANCE HERE
    async def resistance(self):
        print('resistance')
        content = Ohms().res()
        res_equation, amps, resistance, volts = content

        def update_label_text(text):
            self.l1.text = text

        #self.main_text.bind(on_text_validate=self.update_text)
        self.main_text.text = "" 
        self.l1.text = f'You have {amps:.2f} amps and {volts} voltage\n\n How many volts do you have?'
        
        await ak.event(self.main_text, 'on_text_validate')
        print(res_equation)
 
        if self.main_text.text == str(f"{res_equation:.2f}"):
            Clock.schedule_once(lambda dt: update_label_text('Great Job!'))
            print('if is working')
          
    
        else:
            Clock.schedule_once(lambda dt: update_label_text("Sorry, that's incorrect"))
            print('else is working')
            
                

class OhmsLawApp(App):
    pass

OhmsLawApp().run()