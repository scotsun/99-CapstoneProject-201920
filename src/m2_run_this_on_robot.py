"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Daniel Pollack..
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()

def real_thing():
    robot=rosebot.RoseBot()
    import tkinter
    from tkinter import ttk
    import mqtt_remote_method_calls as com
    import shared_gui_delegate_on_robot as sharegui
    my_delegate=sharegui.DelegateThatReceives(robot)
    mqtt_receiver=com.MqttClient(my_delegate)
    mqtt_receiver.connect_to_pc()
    time.sleep(1)
    while True:
        time.sleep(0.01)

    print()





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()