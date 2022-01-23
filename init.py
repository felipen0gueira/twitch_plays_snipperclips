import nxbt
from nxbt import Buttons
from nxbt import Sticks
import time


nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

print("Connected")



def jumpLeft():

    
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_LEFT"] = True
        lStick["X_VALUE"] = -100
        btPack["L_STICK"] = lStick
        btPack["B"] = True

        print(btPack)
        for x in range(220):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)

def jumpRight():
        btPack = nx.create_input_packet()
        lStick = btPack["L_STICK"]
        lStick["LS_RIGHT"] = True
        lStick["X_VALUE"] = 100
        btPack["L_STICK"] = lStick
        btPack["B"] = True

        print(btPack)
        for x in range(220):
            nx.set_controller_input( controller_index, btPack)

        btPack = nx.create_input_packet()
        nx.set_controller_input( controller_index, btPack)

def right():
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=3)

def left():
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=3)



waitingInput = True

while waitingInput:
    waitingInput = input("Seconds:")
    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=5,  released=0.1, block=False)

    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)

    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=5,  released=0.1, block=False)
    
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)


    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=5,  released=0.1, block=False)
    
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)


    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=5,  released=0.1, block=False)
    
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)

    
    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=5,  released=0.1, block=False)
    
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)


    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=5,  released=0.1, block=False)
    
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)


    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=5,  released=0.1, block=False)
    
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)


    #print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=1.5)")
    #nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=5,  released=0.1, block=False)
    #nx.press_buttons(controller_index, [nxbt.Buttons.B, nxbt.Buttons.L], down=waitingInput, up=0.1, block=False)
    if waitingInput == "1":
        jumpLeft()


    if waitingInput == "2":
        jumpRight()


    if waitingInput == "3":
        right()

    if waitingInput == "4":
        left()




    if(waitingInput == "exit"):
        waitingInput = False


