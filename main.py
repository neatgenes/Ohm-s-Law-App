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
from kivy.uix.image import Image

# TODAY GET THE ALGORITHMS WORKING
# Add two decimal spaces if user doesn't add them. We might want to add 4 decimal places for amps
# Add clock updates from the if statements that start the questions again
# That might be a way to fix the loop - fixed that bitch
# ADD other stuff
# create a way to get a random test
# WORK ON GUI
# create header label and bottom label
# functions will continue running until answered

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
        # BUTTON BINDING
        self.volts_button.bind(on_press=self.volts_udpate)
        self.amps_button.bind(on_press=self.amps_udpate)
        self.res_button.bind(on_press=self.res_udpate)
        

    def menu_setup(self):
        # WIDGETS
        self.main_text = TextInput(size=(self.width, self.height*.15), multiline=False, background_color=(0,0,0,1), foreground_color=(.2,1,.2,1), font_name='main.ttf')
        self.volts_button = Button(text='Voltage Questions', font_name='main.ttf', color=(.2,1,.2,1), background_color=(0,0,0,1))
        self.amps_button = Button(text='Amperage Questions', font_name='main.ttf', color=(.2,1,.2,1), background_color=(0,0,0,1))
        self.res_button = Button(text='Resistance Questions', font_name='main.ttf', color=(.2,1,.2,1), background_color=(0,0,0,1))
        self.l1 = Label(text=("Ohm's Law Calculation Test"), font_name='main.ttf', color=(.2,1,.2,1))
        self.l2 = Label(font_name='main.ttf', color=(.2,1,.2,1))
        self.l3 = Label(font_name='main.ttf', color=(.2,1,.2,1))
        self.background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)
        self.add_widget(self.l1)
        self.add_widget(self.l2)
        self.add_widget(self.l3)
        self.add_widget(self.main_text)
        self.add_widget(self.volts_button)
        self.add_widget(self.amps_button)
        self.add_widget(self.res_button)
        
# 
    def update_text_size(self, *args):
        # BUTTON RESIZING - THE NAME SUCKS I KNOW, BUT I DON'T FEEL LIKE CHANGING IT NOW
        self.background.height = self.height
        self.background.width = self.width
        self.main_text.size = (self.width, self.height*.15)
        self.volts_button.pos = (0, self.height*.15)
        self.volts_button.size = (self.width/3, self.height*.10)
        self.amps_button.pos = (self.volts_button.width, self.height*.15)
        self.amps_button.size = (self.width/3, self.height*.10)
        self.res_button.pos = (self.volts_button.width*2, self.height*.15)
        self.res_button.size = (self.width/3, self.height*.10)
        self.l1.pos = (self.center_x-(self.l1.width/2), self.center_y+(self.l1.width/2))
        self.l1.font_size = self.center_x/10
        self.l2.pos = (self.center_x-(self.l1.width/2), self.center_y/2)
        self.l2.font_size = self.center_x/10
        self.l3.pos = (self.center_x-(self.l1.width/2), self.center_y+(self.l1.width/2)+(self.l1.font_size*2))
        self.l3.font_size = self.center_x/10
        print(f"width {self.width}\nheight {self.height}")
        
    # BUTTON CALLBACKS    
    def volts_udpate(self, *args):
        Ohms().volts()
        self.amps_running = False
        self.res_running = False
        self.volts_running = True
        ak.start(self.voltage())

    def amps_udpate(self, *args):
        Ohms().amps()
        self.res_running = False
        self.volts_running = False
        self.amps_running = True
        ak.start(self.amperage())

    def res_udpate(self, *args):
        Ohms().res()
        self.amps_running = False
        self.volts_running = False
        self.res_running = True
        ak.start(self.resistance())
    
    # ASYNC FUNCTIONS FOR BUTTONS 
    # Able to fix the loop and make it work with await ak.sleep(). WOOT!
    # functions will continue running until answered
    async def voltage(self):
        while self.volts_running:
            print('voltage')
            content = Ohms().volts()
            voltage_equation, amps, resistance, volts = content
            print(f'volts: {volts} amps: {amps} res: {resistance} result: {voltage_equation}')

            def update_label_text(text):
                self.l1.text = text

            #self.main_text.bind(on_text_validate=self.update_text)
            self.main_text.text = "" 
            self.l3.text = 'Voltage'
            self.l2.text = 'Remember to round to a whole number'
            self.l1.text = f'You have {amps:.4f} amps and {resistance} resistance\nHow many volts do you have?'
            
            await ak.event(self.main_text, 'on_text_validate')
            print(voltage_equation)

            
            if self.main_text.text == str(f"{voltage_equation}"):
                Clock.schedule_once(lambda dt: update_label_text('Great Job!'))
                print('if is working')
                await ak.sleep(2)
                
            
            else:
                Clock.schedule_once(lambda dt: update_label_text("Sorry, that's incorrect\n{voltage_equation} is the right answer"))
                print('else is working')
                await ak.sleep(2)
                
    
    
    # NEED TO ROUND THE NUMBERS AND FIGURE OUT HOW TO SEND RES AS FLOAT
    async def amperage(self):
        while self.amps_running:
            print('amps')
            content = Ohms().amps()
            amps_equation, amps, resistance, volts = content
            print(f'volts: {volts} amps: {amps:.4f} res: {resistance} result: {amps_equation:.2f}')

            def update_label_text(text):
                self.l1.text = text

            self.main_text.text = "" 
            self.l3.text = 'Amperage'
            self.l2.text = 'Remember, only two decimal spaces'
            self.l1.text = f'You have {volts} volts and {resistance} resistance\n\n How many amps do you have?'
            await ak.event(self.main_text, 'on_text_validate')
            print(f"{amps_equation:.2f}")

            if self.main_text.text == str(f"{amps_equation:.2f}"):
                Clock.schedule_once(lambda dt: update_label_text('Great Job!'))
                print('if is working')
                await ak.sleep(2)
                
            else:
                Clock.schedule_once(lambda dt: update_label_text("Sorry, that's incorrect"))
                print('else is working')
                await ak.sleep(2)
            
          

    
    # numbers are too big here past the decimal
    async def resistance(self):
        while self.res_running:
            print('resistance')
            content = Ohms().res()
            res_equation, amps, resistance, volts = content
            print(f'volts: {volts} amps: {amps:.4f} res: {resistance}, result: {res_equation:.4f}')

            def update_label_text(text):
                self.l1.text = text

            #self.main_text.bind(on_text_validate=self.update_text)
            self.main_text.text = "" 
            self.l3.text = 'Resistance'
            self.l2.text = 'Remember, only two decimal spaces'
            self.l1.text = f'You have {amps:.4f} amps and {volts} voltage\n\n How many volts do you have?'
            
            await ak.event(self.main_text, 'on_text_validate')
            print(res_equation)
    
            if self.main_text.text == str(f"{res_equation:.2f}"):
                Clock.schedule_once(lambda dt: update_label_text('Great Job!'))
                print('if is working')
                await ak.sleep(2)
            
        
            else:
                Clock.schedule_once(lambda dt: update_label_text("Sorry, that's incorrect"))
                print('else is working')
                await ak.sleep(2)
            
                

class OhmsLawApp(App):
    pass

OhmsLawApp().run()