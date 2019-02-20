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
import m1_laptop_delegate as m1



def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    laptop_delegate = m1.DelegateLaptop()
    mqtt_sender = com.MqttClient(laptop_delegate)
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
    sprint3_root.configure(background="cornflower blue")
    sprint3_root.geometry("337x340")

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

    # root.mainloop()
    sprint3_root.mainloop()



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
# Sprint 3 personal gui feature
# -----------------------------------------------------------------------------

def m1_sprint3_get_my_frame(window, mqtt_sender):
    panel_label = ttk.Label(window, text="Oil/Metal Detector Controlling Panel",
                            font=("Oil/Metal Detector Controlling Panel", 16))
    panel_label.grid(row=0, column=0)

    frame_1 = ttk.Frame(window, padding=10, borderwidth=20, relief="sunken")
    frame_1.grid(row=1, column=0)

    frame_2 = ttk.Frame(window, padding=10, borderwidth=20, relief="sunken")
    frame_2.grid(row=2, column=0)

    left_speed_label = ttk.Label(frame_1, text="left")
    left_speed_entry = ttk.Entry(frame_1, width=10)
    right_speed_label = ttk.Label(frame_1, text="Right")
    right_speed_entry = ttk.Entry(frame_1, width=10)

    turn_left_button = ttk.Button(frame_1, text="TurnLeft")
    forward_button = ttk.Button(frame_1, text="Forward")
    turn_right_button = ttk.Button(frame_1, text="TurnRight")
    back_button = ttk.Button(frame_1, text="Back")

    park_assist_button = ttk.Button(frame_1, text="Park Assist")

    detect_button = ttk.Button(frame_2, text="Detect")
    remove_object_button = ttk.Button(frame_2, text="Remove Object")

    oil_radio = ttk.Radiobutton(frame_2, text="Oil", value="Oil")
    metal_radio = ttk.Radiobutton(frame_2, text="Metal", value="Metal")

    exit_button = ttk.Button(window, text="Exit")

    # grid the GUI
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)
    turn_left_button.grid(row=3, column=0)
    forward_button.grid(row=3, column=1)
    turn_right_button.grid(row=3, column=2)
    back_button.grid(row=4, column=1)
    park_assist_button.grid(row=4, column=2)

    oil_radio.grid(row=0, column=0)
    metal_radio.grid(row=1, column=0)
    remove_object_button.grid(row=0, column=2)
    detect_button.grid(row=1, column=2)

    exit_button.grid(row=3, column=0)

    # features on radio-buttons
    radio_observer = tkinter.StringVar()
    oil_radio["variable"] = radio_observer
    oil_radio["command"] = lambda: radiobutton_changed(radio_observer)
    metal_radio["variable"] = radio_observer
    metal_radio["command"] = lambda: radiobutton_changed(radio_observer)

    # buttons' commands
    forward_button["command"] = lambda: handler_forward(left_speed_entry=left_speed_entry,
                                                        right_speed_entry=right_speed_entry,
                                                        mqtt_sender=mqtt_sender)
    back_button["command"] = lambda: handler_back(left_speed_entry=left_speed_entry,
                                                  right_speed_entry=right_speed_entry,
                                                  mqtt_sender=mqtt_sender)
    turn_left_button["command"] = lambda: handler_turn_left(left_speed_entry=left_speed_entry,
                                                            right_speed_entry=right_speed_entry,
                                                            mqtt_sender=mqtt_sender)
    turn_right_button["command"] = lambda: handler_turn_right(left_speed_entry=left_speed_entry,
                                                              right_speed_entry=right_speed_entry,
                                                              mqtt_sender=mqtt_sender)
    park_assist_button["command"] =lambda: pass
    detect_button["command"] = lambda: handler_detect(mqtt_sender=mqtt_sender)

    remove_object_button["command"] = lambda: handler_remove_object(mqtt_sender=mqtt_sender)
    exit_button["command"] = lambda: exit()

    # bind the laptop's keyboard to controlling panel (gui)
    window.bind_all('<KeyRelease>', lambda event: handler_stop(event, mqtt_sender))
    window.bind_all('<Key-w>', lambda event: handler_forward(event,
                                                             left_speed_entry=left_speed_entry,
                                                             right_speed_entry=right_speed_entry, mqtt_sender=mqtt_sender))
    window.bind_all('<Key-s>', lambda event: handler_back(event,
                                                          left_speed_entry=left_speed_entry,
                                                          right_speed_entry=right_speed_entry, mqtt_sender=mqtt_sender))
    window.bind_all('<Key-a>', lambda event: handler_turn_left(event,
                                                               left_speed_entry=left_speed_entry,
                                                               right_speed_entry=right_speed_entry, mqtt_sender=mqtt_sender))

    window.bind_all('<Key-d>', lambda event: handler_turn_right(event,
                                                                left_speed_entry=left_speed_entry,
                                                                right_speed_entry=right_speed_entry, mqtt_sender=mqtt_sender))
    window.bind_all('<Key-n>', lambda event: handler_remove_object(event, mqtt_sender=mqtt_sender))

    window.bind_all('<Key-m>', lambda event: handler_detect(event, radio_observer=radio_observer, mqtt_sender=mqtt_sender))
    return frame_1, frame_2

def radiobutton_changed(radio_observer):
    mode = radio_observer.get()
    print('The detector is turned to', mode, 'detecting mode.')
    return mode

def handler_stop(event, mqtt_sender):
    if event.keysym is "a":
        print("stop")
        mqtt_sender.send_message("stop")
    elif event.keysym is "w":
        print("stop")
        mqtt_sender.send_message("stop")
    elif event.keysym is "s":
        print("stop")
        mqtt_sender.send_message("stop")
    elif event.keysym is "d":
        print("stop")
        mqtt_sender.send_message("stop")


def handler_forward(event=None, left_speed_entry=None, right_speed_entry=None, mqtt_sender=None):
    left_speed = int(left_speed_entry.get())
    right_speed = int(right_speed_entry.get())
    if event is None:
        print('You may press <Key-w> to implement the function')
    else:
        mqtt_sender.send_message("forward", [left_speed, right_speed])
        print('Go forward!')
        print('left', left_speed, 'right', right_speed)


def handler_back(event=None, left_speed_entry=None, right_speed_entry=None, mqtt_sender=None):
    left_speed = -int(left_speed_entry.get())
    right_speed = -int(right_speed_entry.get())
    if event is None:
        print('You may press <Key-s> to implement the function')
    else:
        mqtt_sender.send_message('backward', [left_speed, right_speed])
        print('Go back!')
        print('left', left_speed, 'right', right_speed)


def handler_turn_left(event=None, left_speed_entry=None, right_speed_entry=None, mqtt_sender=None):
    left_speed = -int(left_speed_entry.get())
    right_speed = int(right_speed_entry.get())
    if event is None:
        print('You may press <Key-a> to implement the function')
    else:
        mqtt_sender.send_message('left', [left_speed, right_speed])
        print('Turn left!')
        print('left', left_speed, 'right', right_speed)


def handler_turn_right(event=None, left_speed_entry=None, right_speed_entry=None, mqtt_sender=None):
    left_speed = int(left_speed_entry.get())
    right_speed = -int(right_speed_entry.get())
    if event is None:
        print('You may press <Key-d> to implement the function')
    else:
        mqtt_sender.send_message('right', [left_speed, right_speed])
        print('Turn right!')
        print('left', left_speed, 'right', right_speed)

def handler_park_assist(event=None, left_speed_entry=None, right_speed_entry=None, mqtt_sender=None):
    left_speed = int(left_speed_entry.get())
    right_speed = -int(right_speed_entry.get())
    if event is None:
        print('You may press <Key-p> to implement the function')
    else:
        mqtt_sender.send_message('m1_sprint3_park_assist', [left_speed, right_speed])


def handler_remove_object(event=None, mqtt_sender=None):
    if event is None:
        print("You may press <Key-n> to implement the function")
    else:
        mqtt_sender.send_message('m1_sprint3_clear_path')
        print("Removing")


def handler_detect(event=None, radio_observer=None, mqtt_sender=None):
    mode = radiobutton_changed(radio_observer)
    # print('The detector is turned to', mode, 'detecting mode.')
    if event is None:
        print("You may press <Key-m> to implement the function")
    else:
        mqtt_sender.send_message('m1_sprint3_detect', [mode])

main()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()