import nxbt
import time

nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

print("Connected")

time.sleep(10)

nx.press_buttons(controller_idx, [nxbt.Buttons.B], down=1.0)

nx.tilt_stick(controller_idx, Sticks.RIGHT_STICK, -100, 0, tilted=2.0)


