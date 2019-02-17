"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Scott Sun.
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
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project")

    personal_root = tkinter.Tk()
    personal_root.title("Personal Feature")
    sprint3_root = tkinter.Tk()
    sprint3_root.title("Metal-and-Oil Detector")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    # main_frame = ttk.Frame(root, padding=10)
    # main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    # teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, \
    # ColorSensor_driving_frame, IR_driving_frame, camera_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # m1_get_my_frame(personal_root, mqtt_sender)

    m1_sprint3_get_my_frame(sprint3_root, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    # grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame,
    #             ColorSensor_driving_frame, IR_driving_frame, camera_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()




def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    ColorSensor_driving_frame = shared_gui.get_ColorSensor_driving_frame(main_frame, mqtt_sender)
    IR_driving_frame = shared_gui.get_IR_driving_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.get_camera_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, drive_system_frame, \
           sound_system_frame, ColorSensor_driving_frame, IR_driving_frame, \
           camera_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame,
                sound_system_frame, ColorSensor_driving_frame, IR_driving_frame,
                camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=3, column=0)
    sound_system_frame.grid(row=0, column=1)
    ColorSensor_driving_frame.grid(row=1, column=1)
    IR_driving_frame.grid(row=2, column=1)
    camera_frame.grid(row=3, column=1)

# -----------------------------------------------------------------------------
# Sprint 2 personal feature
# -----------------------------------------------------------------------------

def m1_get_my_frame(window, mqtt_sender):
    # frame
    frame = ttk.Frame(window, padding=10, borderwidth=10, relief="ridge")
    frame.grid()

    # feature 9
    inches_label = ttk.Label(frame, text="Inches close to")
    inches_entry = ttk.Entry(frame, width=8)
    speed_label = ttk.Label(frame, text="Speed moving forward")
    speed_entry = ttk.Entry(frame, width=8)
    beep_rate_label = ttk.Label(frame, text="Beep Rate")
    beep_rate_entry = ttk.Entry(frame, width=8)
    acceleration_label = ttk.Label(frame, text="Acceleration")
    acceleration_entry = ttk.Entry(frame, width=8)

    feature_nine_person_one_button = ttk.Button(frame, text="Feature 9")

    inches_label.grid(row=0, column=0)
    inches_entry.grid(row=1, column=0)
    speed_label.grid(row=0, column=2)
    speed_entry.grid(row=1, column=2)
    beep_rate_label.grid(row=3, column=0)
    beep_rate_entry.grid(row=4, column=0)
    acceleration_label.grid(row=3, column=2)
    acceleration_entry.grid(row=4, column=2)

    feature_nine_person_one_button.grid()

    feature_nine_person_one_button["command"] = lambda: (
        handler_feature_nine_person_one(inches_entry, speed_entry, beep_rate_entry, acceleration_entry, mqtt_sender))

    # feature 10
    spin_direction_label = ttk.Label(frame, text="Direction")
    note_label = ttk.Label(frame, text="1 for clockwise; 0 for counter-clockwise")
    spin_direction_entry = ttk.Entry(frame, width=8)
    spin_speed_label = ttk.Label(frame, text="Spin Speed")
    spin_speed_entry = ttk.Entry(frame, width=8)

    feature_ten_person_one_button = ttk.Button(frame, text="Feature 10")

    spin_direction_label.grid()
    spin_direction_entry.grid()
    note_label.grid()
    spin_speed_label.grid()
    spin_speed_entry.grid()
    feature_ten_person_one_button.grid()

    feature_ten_person_one_button["command"] = lambda: (
        handler_feature_ten_person_one(inches_entry, speed_entry, beep_rate_entry, acceleration_entry,
                                       spin_direction_entry, spin_speed_entry, mqtt_sender)
    )

    return frame

def handler_feature_nine_person_one(inches_entry, speed_entry, beep_rate_entry, acceleration_entry, mqtt_sender):
    inches = float(inches_entry.get())
    speed = float(speed_entry.get())
    beep_rate = int(beep_rate_entry.get())
    acceleration = int(acceleration_entry.get())
    mqtt_sender.send_message("m1_Go_with_IR_and_beeps", [inches, speed, beep_rate, acceleration])

def handler_feature_ten_person_one(inches_entry, speed_entry, beep_rate_entry, acceleration_entry,
                                       spin_direction_entry, spin_speed_entry, mqtt_sender):
    inches = float(inches_entry.get())
    speed = float(speed_entry.get())
    beep_rate = int(beep_rate_entry.get())
    acceleration = int(acceleration_entry.get())
    spin_direction = int(spin_direction_entry.get())
    spin_speed = float(spin_speed_entry.get())
    mqtt_sender.send_message("m1_Find_Go_with_IR_and_beeps", [
        inches, speed, beep_rate, acceleration, spin_direction, spin_speed
    ])
    pass

# -----------------------------------------------------------------------------
# Sprint 3 personal feature
# -----------------------------------------------------------------------------

def m1_sprint3_get_my_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=10, relief="ridge")

    control_panel_label = ttk.Label(frame, text="Detector Controlling Panel")

    left_speed_label = ttk.Label(frame, text="left")
    left_speed_entry = ttk.Entry(frame, width=10)
    right_speed_label = ttk.Label(frame, text="Right")
    right_speed_entry = ttk.Entry(frame, width=10)

    turn_left_button = ttk.Button(frame, text="TurnLeft")
    forward_button = ttk.Button(frame, text="Forward")
    turn_right_button = ttk.Button(frame, text="TurnRight")
    back_button = ttk.Button(frame, text="Back")

    locations_label = ttk.Label(frame, text="Locations:")

    oil_label = ttk.Label(frame, text="Oil")
    oil_location_entry = ttk.Entry(frame, width=10)
    oil_location_entry.insert(0, "N/A")

    metal_label = ttk.Label(frame, text="Metal")
    metal_location_entry = ttk.Entry(frame, width=10)

    # grid the GUI
    control_panel_label.grid(row=0, column=2)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)
    turn_left_button.grid(row=3, column=0)
    forward_button.grid(row=3, column=1)
    turn_right_button.grid(row=3, column=2)
    back_button.grid(row=4, column=1)
    locations_label.grid(row=1, column=3)
    oil_label.grid(row=2, column=3)
    oil_location_entry.grid(row=2, column=4)
    metal_label.grid(row=3, column=3)
    metal_location_entry.grid(row=3, column=4)

    return frame



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()