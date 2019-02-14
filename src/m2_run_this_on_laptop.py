"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Daniel Pollack.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender= com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    #root=tkinter.Tk()
    #root.title('Main Frame')
    root2=tkinter.Tk()
    root2.title('Personal Frame')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    #main_frame=ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    #main_frame.grid()
    personal_frame=ttk.Frame(root2, padding=10, borderwidth=5, relief="groove")
    personal_frame.grid()

    #teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, IR_driving_frame,ColorSensor_driving_frame,camera_frame=get_shared_frames(main_frame, mqtt_sender)
    control_frame, personal_frame2,arm_frame,IR_driving_frame,teleoperations_frame=get_personal_frame(personal_frame,mqtt_sender)



    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    #grid_frames(teleop_frame,arm_frame,control_frame,drive_system_frame,sound_system_frame,IR_driving_frame,ColorSensor_driving_frame,camera_frame)
    grid_personal_frames(control_frame,personal_frame2,arm_frame,IR_driving_frame,teleoperations_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    #root.mainloop()
    root2.mainloop()
def get_personal_frame(personal_frame,mqtt_sender):
    import shared_gui
    teleoperations_frame=shared_gui.get_teleoperation_frame(personal_frame,mqtt_sender)
    arm_and_claw_frame=shared_gui.get_arm_frame(personal_frame,mqtt_sender)
    control_frame=shared_gui.get_control_frame(personal_frame,mqtt_sender)
    personal_frame2=shared_gui.get_camera_frame(personal_frame,mqtt_sender)
    IR_driving_frame=shared_gui.get_IR_driving_frame(personal_frame,mqtt_sender)
    return(control_frame,personal_frame2,arm_and_claw_frame,IR_driving_frame,teleoperations_frame)

def get_shared_frames(main_frame, mqtt_sender):
    import shared_gui
    camera_frame=shared_gui.get_camera_frame(main_frame,mqtt_sender)
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
    drive_system_frame=shared_gui.get_drive_system_frame(main_frame,mqtt_sender)
    sound_system_frame=shared_gui.get_sound_system_frame(main_frame,mqtt_sender)
    IR_driving_frame=shared_gui.get_IR_driving_frame(main_frame,mqtt_sender)
    ColorSensor_driving_frame=shared_gui.get_ColorSensor_driving_frame(main_frame,mqtt_sender)
    return(teleop_frame,arm_frame,control_frame,drive_system_frame,sound_system_frame,IR_driving_frame,ColorSensor_driving_frame,camera_frame)
    pass

def grid_personal_frames(control_frame,personal_frame,arm_and_claw_frame,IR_driving_frame,teleoperations_frame):
    IR_driving_frame.grid(row=3,column=0)
    teleoperations_frame.grid(row=4,column=0)
    arm_and_claw_frame.grid(row=2,column=0)
    personal_frame.grid(row=1,column=0)
    control_frame.grid(row=0,column=0)
    pass

def grid_frames(teleop_frame, arm_frame, control_frame,drive_system_frame,sound_system_frame,IR_driving_frame,ColorSensor_driving_frame,camera_frame):
    camera_frame.grid(row=3,column=1)
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=1)
    control_frame.grid(row=2,column=0)
    drive_system_frame.grid(row=3,column=0)
    IR_driving_frame.grid(row=2,column=1)
    sound_system_frame.grid(row=4,column=0)
    ColorSensor_driving_frame.grid(row=4,column=1)
    pass


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()