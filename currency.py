import math
from random import randint
import turtle
import time

hours_passed = 0
# Set up screen
screen = turtle.Screen()
screen.title("Alarm Clock")
canvas = turtle.Turtle()
canvas.speed(0)  # Turns drawing speed off
# Constants defining positions of elements on clock face
HOUR_HAND_LENGTH = 80
MINUTE_HAND_LENGTH = 60
SECOND_HAND_LENGTH = 40
CENTER_X = 0
CENTER_Y = -75
RADIUS = 125
# Variables keeping track of state
seconds_passed = 0
hour_hand_angle = None
minute_hand_angle = None
second_hand_angle = None
timer_started = False
beeping = False
# Function definitions
def update_hands():
    """Updates angles of hour/minute/second hands based on number of seconds passed."""
    nonlocal hours_passed, minute_hand_angle, second_hand_angle
    
    # Calculate new angles for hands
    hours = int((hours_passed % 12 + 12) % 12)   # Hours passed since midnight
    mins = int(math.floor(minutes_passed))     # Minutes passed after full hour
    secs = int(math.floor(seconds_passed))     # Seconds passed after full minute
    
    hour_hand_angle = ((360 / 12) * hours)      # Angle corresponding to position of hour hand
    minute_hand_angle = ((360 / 60) * mins)    # Angle corresponding to position of minute hand
    second_hand_angle = ((360 / 60) * secs)    # Angle corresponding to position of second hand
    
def move_hands():
    """Moves hands according to their respective angle values"""
    nonlocal hour_hand_angle, minute_hand_angle, second_hand_angle
    
    # Move hands to appropriate locations based on calculated angles
    canvas.setheading(90-hour_hand_angle)       # Rotate hour hand counterclockwise
    canvas.forward(HOUR_HAND_LENGTH)           # Draw hour hand
    canvas.setheading(-minute_hand_angle+90)  # Rotate minute hand anti-clockwise around hour hand
    canvas.forward(MINUTE_HAND_LENGTH)         # Draw minute hand
    canvas.setheading(-second_hand_angle+90)   # Rotate second hand anti-clockwise around minute hand
    canvas.forward(SECOND_HAND_LENGTH)         # Draw second hand
    
    
def start_timer():
    """Starts countdown until next interval boundary (e.g., every hour, etc.)"""
    nonlocal seconds_passed, timer_started
    
    while True:
        if seconds_passed >= 3600:
            break
        
        elif seconds_passed == 0:
            print("Starting over from scratch!")
            timer_started = True
            
        else:
            time.sleep(1)
            seconds_passed += 1
            
    
        
def stop_timer():
    """Stops currently running timer"""
    pass
    
def toggle_beeper():
    """Plays sound effect once per click"""
    nonlocal beeping
    beeping = not beeping
    
    if beeping:
        freq = randint(800, 1000)          # Generate frequency between 800 Hz and 1 kHz
        dur = randint(50, 200)/1000        # Generate duration between.5 sec and 2 sec
        winsound.Beep(freq, dur)
        
    return
# Main Loop
while True:
    try:
        # Update variables tracking state
        now = datetime.now()                 
        hours_passed = float(now.strftime("%H.%M")) / 60  
        minutes_passed = float(now.strftime("%M.")) + \
                         float(now.strftime("%S")) / 60
        seconds_passed = float(now.strftime(".%S"))
    
        # Handle user input
        keypress = screen.getch().decode('utf-8')
        if ord(keypress) == 32:               # Spacebar pressed
            if timer_started:
                stop_timer()
                
            else: 
                start_timer()
                    
        elif ord(keypress) == 13:             # Enter/Return pressed
            toggle_beeper()
                
        # Clear old display and redraw clock face    
        canvas.clear()                      
        canvas.penup()                       
        canvas.goto(CENTER_X, CENTER_Y)      
        canvas.pendown()                     
        canvas.circle(RADIUS)               
        canvas.penup()                       
        canvas.goto(CENTER_X, CENTER_Y-(RADIUS*2)-10)        
        canvas.write("{}:{}:{}".format(int(hours), int(mins), int(secs)), font=("Courier", 12, "bold"), align="center") 
    
        # Update hands with new angles
        update_hands()
        move_hands()
        
        # Wait before updating again
        time.sleep(.1)
        
    except KeyboardInterrupt:              # Allow exit via keyboard interrupt
        sys.exit()