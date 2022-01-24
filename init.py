import nxbt
from nxbt import Buttons
from nxbt import Sticks
import time
import random


nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

print("Connected")



def jumpLeft():
        print("jumpLeft()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_LEFT"] = True
        lStick["X_VALUE"] = -100
        btPack["L_STICK"] = lStick
        btPack["B"] = True

        for x in range(220):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)

def jumpRight():
        print("jumpRight()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_RIGHT"] = True
        lStick["X_VALUE"] = 100
        btPack["L_STICK"] = lStick
        btPack["B"] = True

        for x in range(220):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)

def upCut():
        print("upCut()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_UP"] = True
        lStick["Y_VALUE"] = 100
        btPack["L_STICK"] = lStick

        for x in range(220):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_UP"] = True
        lStick["Y_VALUE"] = 100
        btPack["L_STICK"] = lStick
        btPack["A"] = True

        print(btPack)
        for x in range(30):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)


def downCut():
    
        print("downCut()")
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_DOWN"] = True
        lStick["Y_VALUE"] = -100
        btPack["L_STICK"] = lStick

        for x in range(220):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_DOWN"] = True
        lStick["Y_VALUE"] = -100
        btPack["L_STICK"] = lStick
        btPack["A"] = True

        print(btPack)
        for x in range(30):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)

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




waitingInput = True

ready = input("Ready?")

while waitingInput:
    waitingInput = str(random.randint(1, 13))#input("Seconds:")
    print(waitingInput)
    #time.sleep(2)

    if waitingInput == "1":
        jumpLeft()

    if waitingInput == "2":
        jumpRight()

    if waitingInput == "3":
        right()

    if waitingInput == "4":
        left()

    if waitingInput == "5":
        up()

    if waitingInput == "6":
        down()

    if waitingInput == "7":
        jump()

    if waitingInput == "8":
        cut()

    if waitingInput == "9":
        clockwise()

    if waitingInput == "10":
        anticlockwise()

    if waitingInput == "11":
        recover()

    if waitingInput == "12":
        upCut()

    if waitingInput == "13":
        downCut()







    if(waitingInput == "exit"):
        waitingInput = False


