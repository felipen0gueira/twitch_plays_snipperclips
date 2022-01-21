import nxbt
from nxbt import Buttons
from nxbt import Sticks
import time

nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

print("Connected")


waitingInput = True

while waitingInput:
    waitingInput = input("Seconds:")
    print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, tilted=1.5,  released=0.1, block=False)

    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)

    print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 100, 0, tilted=1.5,  released=0.1, block=False)
    
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)


    print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, -100, tilted=1.5,  released=0.1, block=False)
    
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)


    print("nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, tilted=1.5,  released=0.1, block=False)
    
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)

    
    print("nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, -100, 0, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, -100, 0, tilted=1.5,  released=0.1, block=False)
    
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)


    print("nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, 100, 0, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, 100, 0, tilted=1.5,  released=0.1, block=False)
    
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)


    print("nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, 0, -100, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, 0, -100, tilted=1.5,  released=0.1, block=False)
    
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)


    print("nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, 0, 100, tilted=1.5)")
    nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, 0, 100, tilted=1.5,  released=0.1, block=False)
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput, up=0.1, block=False)

    if(waitingInput == "exit"):
        waitingInput = False


