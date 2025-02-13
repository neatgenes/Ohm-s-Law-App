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
from random import randint
#import asyncio

# CLEAN UP CODE TODAY
# Highlight colors of volts, amps, res, etc.
# Add scoring system - done, we can add functionality to it later. Next we should try to get some other quizes on here.
# Add correct answer
# Make text input appear only when you select a test
# Add two decimal spaces if user doesn't add them. We might want to add 4 decimal places for amps
# Equation for leds and what resistor you need
# adding capacitors in series and parallel
# voltage and amps for parallel and series circuit
# Add voltage drop
# series/parallel circuit resistance calculations
# Tau time canstat = resistance * capacitance
# Resistance for parallel circuits


# NEED A LABEL ON THE LEFT THAT SHOW'S WHAT QUESTION YOU'RE ON
# NEED TO SHOW HOW MANY YOU GOT RIGHT AT THE END
class Main(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_setup()
        # upon widget size change, update_text_size is called
        self.bind(size=self.update_text_size)
        # BUTTON BINDING
        self.ohms_test_button.bind(on_press=self.on_press) # formally volts_button
        #self.amps_button.bind(on_press=self.amps_udpate)
        self.exit_button.bind(on_press=self.exit_update)
        #self.test_button.bind(on_press=self.exit_update)
        self.main_text.bind(on_text_validation=self.text_validation)
        #self.validation_event = asyncio.Event()
        self.counter = 1  
        self.answer_counter = 0 
        
    def menu_setup(self):
        # WIDGETS
        # WORKING ON SCORE BUTTON
        self.main_text = TextInput(size=(self.width, self.height*.15), multiline=False, background_color=(0,0,0,1), foreground_color=(.2,1,.2,1), font_name='main.ttf')
        self.ohms_test_button = Button(text="Ohm's Law Test", font_name='main.ttf', color=(.2,1,.2,1), background_color=(0,0,0,1))
        self.amps_button = Button(text="Ohm's Law Calculation Test", font_name='main.ttf', color=(.2,1,.2,1), background_color=(0,0,0,1))
        self.exit_button = Button(text='Exit Test', font_name='main.ttf', color=(.2,1,.2,1), background_color=(0,0,0,1))
        #self.test_button = Button(text='TEST')
        self.score = Label(text="score: 0/10", font_name='main.ttf', color=(.2,1,.2,1))
        self.l1 = Label(text=("Ohm's Law Calculation Test"), font_name='main.ttf', color=(.2,1,.2,1))
        self.l2 = Label(font_name='main.ttf', color=(.2,1,.2,1))
        self.l3 = Label(font_name='main.ttf', color=(.2,1,.2,1))
        self.background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False) #, allow_stretch=True, keep_ratio=False
        self.add_widget(self.background)
        self.add_widget(self.l1)
        self.add_widget(self.l2)
        self.add_widget(self.l3)
        #self.add_widget(self.main_text)
        #self.add_widget(self.test_button)
        self.add_widget(self.ohms_test_button)
        self.add_widget(self.amps_button)
        self.add_widget(self.exit_button)
        #self.add_widget(self.score)
        
    def update_text_size(self, *args):
        # BUTTON RESIZING - THE NAME SUCKS I KNOW, BUT I DON'T FEEL LIKE CHANGING IT NOW
        self.background.height = self.height
        self.background.width = self.width
        self.main_text.size = (self.width, self.height*.15)
        self.ohms_test_button.pos = (0, self.height*.15)
        self.ohms_test_button.size = (self.width/3, self.height*.10)
        self.amps_button.pos = (self.ohms_test_button.width, self.height*.15)
        self.amps_button.size = (self.width/3, self.height*.10)
        self.exit_button.pos = (self.ohms_test_button.width*2, self.height*.15)
        self.exit_button.size = (self.width/3, self.height*.10)
        self.l1.pos = (self.center_x-(self.l1.width/2), self.center_y+(self.l1.width/2))
        self.l1.font_size = self.center_x/10
        self.l2.pos = (self.center_x-(self.l1.width/2), self.center_y/2)
        self.l2.font_size = self.center_x/10
        self.l3.pos = (self.center_x-(self.l1.width/2), self.center_y+(self.l1.width/2)+(self.l1.font_size*2)+50)
        self.l3.font_size = self.center_x/10
        self.score.pos = (self.width-100, self.height-100)
        print(f"width {self.width}\nheight {self.height}")

    def on_press(self, *args):
        self.counter = 0
        self.menu()
        
    async def text_validation(self):
        pass

    def exit_update(self, *args):
        self.main_text.text = "done"
        self.counter = 5
        self.answer_counter = 0
        self.ohms_test_button.disabled = False
        self.l1.text = "Ohm's Law Calculation Test"
        self.l2.text = ""
        self.l3.text = ""
        if self.main_text in self.children and self.score in self.children:
            self.score.text = "score: 0/10"
            self.remove_widget(self.score)
            self.remove_widget(self.main_text)
    
    def exit(self, *args):
        pass

    def menu(self, *args):
        # NEED AN IF STATEMENT HERE OR EXCEPTION IF THE WIDGET EXISTS, OPPOSITE FOR THE BOTTOM
        #self.add_widget(self.main_text)
        if self.counter <= 10:
            print(self.children)
            if self.main_text not in self.children and self.score not in self.children:
                self.add_widget(self.score)
                self.add_widget(self.main_text)

            print("WidgetException")
            self.counter += 1
            self.ohms_test_button.disabled = True
            number = randint(0, 3)
            print('main menu')
           # menu_running = True
            self.l1.text = "Ohm's Law Calculation Test"
            self.l2.text = ""
            self.l3.text = ""
            if number == 0:
                #self.volts_udpate()
                ak.start(self.voltage())
            elif number == 1:
                #self.amps_udpate()
                ak.start(self.amperage())
            elif number == 2:
                #self.res_udpate()
                #ak.start(self.resistance())
                ak.start(self.leds())
            elif number == 3:
                ak.start(self.resistance())
            else: 
                pass
        else:
            menu_running = True
            self.l1.text = "Ohm's Law Calculation Test"
            self.l2.text = ""
            self.l3.text = ""
            self.ohms_test_button.disabled = False
            self.answer_counter = 0
            if self.main_text in self.children and self.score in self.children:
                self.score.text = "score: 0/10"
                self.remove_widget(self.main_text)
                self.remove_widget(self.score)

    def answer_counter_funct(self):
        # have this got to 0 if the exit button is pressed
        self.answer_counter += 1
        print(f" answer counter: {self.answer_counter}")
        for i in range(0, 11):
            if self.answer_counter == i:
                mynum = "score : " + str(i) + "/10"
                self.score.text = mynum
        #if self.answer_counter == 1:
         #   self.score.text = "1/10"       

    async def voltage(self):
        print(self.counter)
        #self.volts_running = True
        print('voltage')
        content = Ohms().volts()
        voltage_equation, amps, resistance, volts = content
        #print(f'volts: {volts} amps: {amps} res: {resistance} result: {voltage_equation}')

        def update_label_text(text):
            self.l1.text = text


        #self.main_text.bind(on_text_validate=self.update_text)
        self.main_text.text = "" 
        self.l3.text = 'Voltage'
        self.l2.text = 'Remember to round to a whole number'
        self.l1.text = f'You have {amps:.4f} amps and {resistance} resistance\nHow many volts do you have?'
        tasks = await ak.wait_any(
            ak.event(self.main_text, 'on_text_validate'),
            ak.event(self.exit_button, "on_press"),    
        )
        
        print('volts moving on')
        
        if self.main_text.text == str(f"{voltage_equation}"):
            print('made it to if')
            Clock.schedule_once(lambda dt: update_label_text(f'Great Job!\n{voltage_equation} is correct!'))
            await ak.sleep(2)
            self.volts_running = True
            self.answer_counter_funct()
            self.menu()

        elif tasks[1].finished:
            print("finished, setting counter to 5")
            self.counter = 12
            self.menu()

        else:
            print('made it to else')
            Clock.schedule_once(lambda dt: update_label_text(f"Sorry, that's incorrect\n{voltage_equation} is the right answer"))
          #  await ak.sleep(2)
            await ak.sleep(2)
            self.menu()
         #   self.volts_running = True
                
    
    async def amperage(self):
        print(self.counter)
        print('amps')
        content = Ohms().amps()
        amps_equation, amps, resistance, volts = content
        #print(f'volts: {volts} amps: {amps:.4f} res: {resistance} result: {amps_equation:.2f}')

        def update_label_text(text):
            self.l1.text = text

        self.main_text.text = "" 
        self.l3.text = 'Amperage'
        self.l2.text = 'Remember, only two decimal spaces'
        self.l1.text = f'You have {volts} volts and {resistance} resistance\nHow many amps do you have?'
        tasks = await ak.wait_any(
            ak.event(self.main_text, 'on_text_validate'),
            ak.event(self.exit_button, "on_press"),    
        )
        print('amps moving on')

        if self.main_text.text == str(f"{amps_equation:.2f}"):
            Clock.schedule_once(lambda dt: update_label_text(f'Great Job!\n{amps_equation:.2f} is correct!'))
            await ak.sleep(2)
            self.answer_counter_funct()
            self.menu()
            
            
        elif tasks[1].finished:
            self.counter = 12
            self.menu()

        else:
            Clock.schedule_once(lambda dt: update_label_text(f"Sorry, that's incorrect\n{amps_equation:.2f} is the answer"))
            await ak.sleep(2)
            self.menu()
        

    async def resistance(self):
        print(self.counter)
        print('resistance')
        content = Ohms().res()
        res_equation, amps, resistance, volts = content

        def update_label_text(text):
            self.l1.text = text

        #self.main_text.bind(on_text_validate=self.update_text)
        self.main_text.text = "" 
        self.l3.text = 'Resistance'
        self.l2.text = 'Remember, only two decimal spaces'
        self.l1.text = f'You have {amps:.4f} amps and {volts} voltage\n\n How many volts do you have?'
        
        tasks = await ak.wait_any(
            ak.event(self.main_text, 'on_text_validate'),
            ak.event(self.exit_button, "on_press"),    
        )
        print('res moving on')

        if self.main_text.text == str(f"{res_equation:.2f}"):
            Clock.schedule_once(lambda dt: update_label_text(f'Great Job!\n{res_equation:.2f} is correct'))
            print('if is working')
            await ak.sleep(2)
            self.answer_counter_funct()
            self.menu()

        elif tasks[1].finished:
            self.counter = 12
            self.menu()
    
        else:
            Clock.schedule_once(lambda dt: update_label_text(f"Sorry, that's incorrect\n{res_equation:.2f} is the answer"))
            print('else is working')
            await ak.sleep(2)
            self.menu()


    async def leds(self):
        # ADD TO PYTHON CLASS THAT VOLTAGE HAS TO BE HIGHER THAN 3
        print('LED')
        content = Ohms().leds()
        #self.led_v, self.ma, self.v, self.led_equation
        led_v, ma, v, led_equation = content

        def update_label_text(text):
            self.l1.text = text

        #self.main_text.bind(on_text_validate=self.update_text)
        self.main_text.text = "" 
        self.l3.text = 'LEDs'
        self.l2.text = ''
        # f"If you have an LED that requires {led_v} volts and {ma} miliAmps using a {v} volt battery to power them, what resistance do you need?"
        self.l1.text = f'You have an LED that requires {led_v} volts\nand {ma} MiliAmps\nas well as a battery that has {v} volts\nHow many Ohms of resistance do you need??'
        
        tasks = await ak.wait_any(
            ak.event(self.main_text, 'on_text_validate'),
            ak.event(self.exit_button, "on_press"),    
        )
        print('res moving on')

        if self.main_text.text == str(f"{led_equation}"):
            Clock.schedule_once(lambda dt: update_label_text(f'Great Job!\n{led_equation} is correct'))
            print('if is working')
            await ak.sleep(2)
            self.answer_counter_funct()
            self.menu()

        elif tasks[1].finished:
            self.counter = 12
            self.menu()
    
        else:
            Clock.schedule_once(lambda dt: update_label_text(f"Sorry, that's incorrect\n{led_equation:.2f} is the answer"))
            print('else is working')
            await ak.sleep(2)
            self.menu()
            
class OhmsLawApp(App):
    pass

OhmsLawApp().run()
