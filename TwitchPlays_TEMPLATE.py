# Written by DougDoug and DDarknut

# Hello! This file contains the main logic to process Twitch chat and convert it to game commands.
# The code is written in Python 3.X
# There are 2 other files needed to run this code:
    # TwitchPlays_KeyCodes.py contains the key codes and functions to press keys in-game. You should not modify this file.
    # TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

# The source code primarily comes from:
    # Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    # PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/
    # DDarknut's message queue and updates to the Twitch networking code

# Disclaimer: 
    # This code is NOT intended to be professionally optimized or organized.
    # We created a simple version that works well for livestreaming, and I'm sharing it for educational purposes.

##########################################################

TWITCH_CHANNEL = 'felipen0g' # Replace this with your Twitch username. Must be all lowercase.

##########################################################

#import keyboard
import TwitchPlays_Connection
#import pydirectinput
import random
#import pyautogui
import concurrent.futures
#from TwitchPlays_KeyCodes import *

import nxbt
from nxbt import Buttons
from nxbt import Sticks
import time


nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)



def jumpLeft():
        print("jumpLeft()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_LEFT"] = True
        lStick["X_VALUE"] = -100
        btPack["L_STICK"] = lStick
        btPack["B"] = True

        for x in range(20):
            nx.set_controller_input( controller_index, btPack)
            time.sleep(1/120)  

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)
        time.sleep(1/120)  

def jumpRight():
        print("jumpRight()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_RIGHT"] = True
        lStick["X_VALUE"] = 100
        btPack["L_STICK"] = lStick
        btPack["B"] = True

        for x in range(20):
            nx.set_controller_input( controller_index, btPack)
            time.sleep(1/120)  

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)
        time.sleep(1/120)  

def upCut():
        print("upCut()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_UP"] = True
        lStick["Y_VALUE"] = 100
        btPack["L_STICK"] = lStick

        for x in range(50):
            nx.set_controller_input( controller_index, btPack)
            time.sleep(1/120)  

        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_UP"] = True
        lStick["Y_VALUE"] = 100
        btPack["L_STICK"] = lStick
        btPack["A"] = True

        for x in range(10):
            nx.set_controller_input( controller_index, btPack)
            time.sleep(1/120)  

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)
        time.sleep(1/120)  


def downCut():
    
        print("downCut()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_DOWN"] = True
        lStick["Y_VALUE"] = -100
        btPack["L_STICK"] = lStick

        for x in range(50):
            nx.set_controller_input( controller_index, btPack)
            time.sleep(1/120)  

        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_DOWN"] = True
        lStick["Y_VALUE"] = -100
        btPack["L_STICK"] = lStick
        btPack["A"] = True

        for x in range(10):
            nx.set_controller_input( controller_index, btPack)
            time.sleep(1/120)  

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)
        time.sleep(1/120)  

def right():
    print("right()")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=0.2)

def left():
    print("left()")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=0.2)

def up():
    
    print("up()")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=2)

def down():
    print("down()")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=2, released=0.1, block=False)

def jump():
    print("jump()")
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=2, up=0.1, block=False)

def cut():
    print("cut()")
    nx.press_buttons(controller_index, [nxbt.Buttons.A], down=0.1, up=0.1, block=False)

def clockwise():
    print("clockwise()")
    nx.press_buttons(controller_index, [nxbt.Buttons.R], down=0.2)


def anticlockwise():
    print("anticlockwise()")
    nx.press_buttons(controller_index, [nxbt.Buttons.L], down=0.2)


def recover():
    print("recover()")
    nx.press_buttons(controller_index, [nxbt.Buttons.Y], down=1.5)


nx.wait_for_connection(controller_index)

print("Connected")

##########################################################

# MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
# This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
# A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch. 
# A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
# You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
MESSAGE_RATE = 0.5
# MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages. 
# e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
# This is helpful for games where too many inputs at once can actually hinder the gameplay.
# Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
MAX_QUEUE_LENGTH = 20  
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 

last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
#pyautogui.FAILSAFE = False

##########################################################

# An optional count down before starting, so you have time to load up the game
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_CHANNEL);

def handle_message(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print("Got the message: [" + msg + "] from user [" + username + "]")

        # Now that you have a chat message, this is where you add your game logic.
        # Use the "HoldKey(KEYCODE)" function to press and hold down a keyboard key.
        # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
        # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
        # Use the pydirectinput library to press or move the mouse

        # I've added some example videogame logic code below:

        ###################################
        # Example GTA V Code 
        ###################################

        if msg == "pulo esquerda":
            jumpLeft()

        if msg == "pulo direita":
            jumpRight()

        if msg == "direita":
            right()

        if msg == "esquerda":
            left()

        if msg == "cima":
            up()

        if msg == "baixo":
            down()

        if msg == "pulo":
            jump()

        if msg == "corta":
            cut()

        if msg == "gira horario":
            clockwise()

        if msg == "gira anti-horario" or msg == "gira antihorario":
            anticlockwise()

        if msg == "recuperar":
            recover()

        if msg == "corte cima":
            upCut()

        if msg == "corte baixo":
            downCut()


        ####################################
        ####################################

    except Exception as e:
        print("Encountered exception: " + str(e))


while True:

    active_tasks = [t for t in active_tasks if not t.done()]

    #Check for new messages
    new_messages = t.twitch_receive_messages();
    if new_messages:
        message_queue += new_messages; # New messages are added to the back of the queue
        message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

    messages_to_handle = []
    if not message_queue:
        # No messages in the queue
        last_time = time.time()
    else:
        # Determine how many messages we should handle now
        r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
        n = int(r * len(message_queue))
        if n > 0:
            # Pop the messages we want off the front of the queue
            messages_to_handle = message_queue[0:n]
            del message_queue[0:n]
            last_time = time.time();

    # If user presses Shift+Backspace, automatically end the program
    #if keyboard.is_pressed('shift+backspace'):
    #    exit()

    if not messages_to_handle:
        continue
    else:
        for message in messages_to_handle:
            if len(active_tasks) <= MAX_WORKERS:
                active_tasks.append(thread_pool.submit(handle_message, message))
            else:
                print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')
