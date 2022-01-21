import nxbt
import time

nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

print("Connected")


waitingInput = True

while waitingInput:
    waitingInput = input("Seconds:")
    nx.press_buttons(controller_index, [nxbt.Buttons.B], down=waitingInput)
    nx.tilt_stick(controller_index, Sticks.RIGHT_STICK, -100, 0, tilted=waitingInput)
    if(waitingInput == "exit"):
        waitingInput = False


