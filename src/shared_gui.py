"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Emily Wilcox, Scott Sun, Daniel Pollack.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drive_system_frame(window, mqtt_sender):
    # Construct the frame
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Drive System")
    speed_label = ttk.Label(frame, text="Speed")
    speed_entry = ttk.Entry(frame)
    time_label = ttk.Label(frame, text="Time")
    time_entry = ttk.Entry(frame)
    inches_time_label = ttk.Label(frame, text="Inches for Time")
    inches_time_entry = ttk.Entry(frame)
    inches_encoder_label = ttk.Label(frame, text="Inches for Encoder")
    inches_encoder_entry = ttk.Entry(frame)

    frame_label.grid(row=0, column=2)
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    time_label.grid(row=1, column=1)
    time_entry.grid(row=2, column=1)
    inches_time_label.grid(row=1, column=3)
    inches_time_entry.grid(row=2, column=3)
    inches_encoder_label.grid(row=1, column=4)
    inches_encoder_entry.grid(row=2, column=4)

    button_go_straight_with_seconds = ttk.Button(frame, text="SecondsMethod")
    button_go_straight_with_seconds.grid(row=4, column=0)

    button_go_for_inches_time_approach = ttk.Button(frame, text="TimeW/Inches")
    button_go_for_inches_time_approach.grid(row=4, column=2)

    button_go_for_inches_encoder_approach = ttk.Button(frame, text="TimeW/Encoder")
    button_go_for_inches_encoder_approach.grid(row=4, column=4)

    # Set command functions
    button_go_straight_with_seconds["command"] = lambda: handle_go_straight_with_seconds(
        time_entry, speed_entry, mqtt_sender)
    button_go_for_inches_time_approach["command"] = lambda: handle_go_for_inches_time_approach(
        inches_time_entry, speed_entry, mqtt_sender)
    button_go_for_inches_encoder_approach["command"] = lambda: handle_go_for_inches_encoder_approach(
        inches_encoder_entry, speed_entry, mqtt_sender)

    return frame


def get_sound_system_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Sound System")

    number_of_beeps_Label= ttk.Label(frame, text="Number of Beeps")
    number_of_beeps_entry = ttk.Entry(frame, width=8)

    frequency_label = ttk.Label(frame, text="Frequency")
    frequency_entry = ttk.Entry(frame, width=8)

    time_label = ttk.Label(frame, text="Time")
    time_entry = ttk.Entry(frame, width=8)

    given_phrase_button = ttk.Label(frame, text="Phrase")
    given_phrase_entry = ttk.Entry(frame, width=8)

    frame_label.grid(row=0, column=1)

    number_of_beeps_Label.grid(row=1, column=0)
    number_of_beeps_entry.grid(row=2, column=0)

    frequency_label.grid(row=3, column=0)
    frequency_entry.grid(row=4, column=0)

    time_label.grid(row=1, column=2)
    time_entry.grid(row=2, column=2)

    given_phrase_button.grid(row=3, column=2)
    given_phrase_entry.grid(row=4, column=2)

    beep_button = ttk.Button(frame, text="Beep")
    beep_button.grid(row=5, column=0)

    play_tone_button = ttk.Button(frame, text="Play Tone")
    play_tone_button.grid(row=5, column=1)

    speak_button = ttk.Button(frame, text="Speak")
    speak_button.grid(row=5, column=2)

    beep_button["command"] = lambda: handle_beep(mqtt_sender,number_of_beeps_entry)
    play_tone_button["command"] = lambda: handle_frequency(mqtt_sender,frequency_entry,time_entry)
    speak_button["command"] = lambda: handle_speak_phrase(mqtt_sender,given_phrase_entry)

    return frame

def get_IR_driving_frame(window,mqtt_sender):
    frame=ttk.Frame(window,padding=10,borderwidth=5,relief="ridge")

    frame.grid()
    frame_label=ttk.Label(frame, text="IR System")

    forward_ir=ttk.Button(frame, text="Forward w/ IR")
    forward_ir_entry=ttk.Entry(frame, width=8)

    backwards_ir=ttk.Button(frame, text="Backward w/ IR")
    backwards_ir_entry=ttk.Entry(frame, width=8)

    speed=ttk.Label(frame, text='Speed')
    speed_entry=ttk.Entry(frame, width=8)

    go_until_distance_with_ir=ttk.Button(frame, text="Forward w/ IR")
    go_until_distance_with_ir_entry=ttk.Entry(frame, width=8)

    delta_ir=ttk.Label(frame,text="Delta")
    delta_entry=ttk.Entry(frame,width=8)

    #These are the positions of the various frames and buttons located in the gui
    speed.grid(row=1,column=0)
    speed_entry.grid(row=2,column=0)

    frame_label.grid(row=0,column=0)

    forward_ir.grid(row=1, column=1)
    forward_ir_entry.grid(row=2, column=1)

    backwards_ir.grid(row=3, column=1)
    backwards_ir_entry.grid(row=4, column=1)

    delta_ir.grid(row=3,column=0)
    delta_entry.grid(row=4,column=0)

    go_until_distance_with_ir.grid(row=5, column=1)
    go_until_distance_with_ir_entry.grid(row=6, column=1)



    forward_ir["command"] = lambda: handle_forward_ir(mqtt_sender,speed_entry, forward_ir_entry)
    backwards_ir["command"] = lambda: handle_backward_ir(mqtt_sender, speed_entry, backwards_ir_entry)
    go_until_distance_with_ir["command"]=lambda: handle_distance_ir(mqtt_sender, speed_entry, go_until_distance_with_ir_entry,delta_entry)

    return(frame)


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################


def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_speed = left_entry_box.get()
    right_speed = right_entry_box.get()
    print("Message Sent")
    mqtt_sender.send_message("forward", [left_speed, right_speed])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_speed = left_entry_box.get()
    right_speed = right_entry_box.get()
    mqtt_sender.send_message("backward", [left_speed, right_speed])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_speed = left_entry_box.get()
    right_speed = right_entry_box.get()
    print('left')
    mqtt_sender.send_message("left", [left_speed, right_speed])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_speed = left_entry_box.get()
    right_speed = right_entry_box.get()
    print('right')
    mqtt_sender.send_message("right", [left_speed, right_speed])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    mqtt_sender.send_message("stop")

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################


def handle_raise_arm(mqtt_sender):
    mqtt_sender.send_message("raise_arm")

    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    

def handle_lower_arm(mqtt_sender):
    mqtt_sender.send_message("lower_arm")
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_calibrate_arm(mqtt_sender):
    mqtt_sender.send_message("calibrate_arm")
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    arm_position_entry=arm_position_entry.get()
    mqtt_sender.send_message("move_arm_to_position",[arm_position_entry])

    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('Check')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('Exit')
    handle_quit(mqtt_sender)
    exit()

###############################################################################
# Handlers for Buttons in the Drive System frame.
###############################################################################
def handle_go_straight_with_seconds(time_entry, speed_entry, mqtt_sender):
    """
    Tells the robot to move straight for a given number of seconds
    :type mqtt_sender: com.MqttClient
    """
    time = int(time_entry.get())
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_straight_using_seconds", [time, speed])


def handle_go_for_inches_time_approach(inches_time_entry, speed_entry, mqtt_sender):

    inches = int(inches_time_entry.get())
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_for_inches_w_time_approach", [inches, speed])


def handle_go_for_inches_encoder_approach(inches_encoder_entry, speed_entry, mqtt_sender):

    inches = int(inches_encoder_entry.get())
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_for_inches_encoder_approach", [inches, speed])

###################################################################################
# handle for Sound System
###################################################################################


def handle_beep(mqtt_sender,number_of_beeps_button):
    number_of_beeps=int(number_of_beeps_button.get())
    print('beep')
    mqtt_sender.send_message("beep_n_times",[number_of_beeps])


def handle_frequency(mqtt_sender,frequency_button,time_button):
    freq=int(frequency_button.get())
    time=int(time_button.get())

    print('frequency')
    mqtt_sender.send_message("play_frequency_for_duration",[freq,time])


def handle_speak_phrase(mqtt_sender,phrase):
    phrase=phrase.get()
    print('Phrase')
    mqtt_sender.send_message("speak_phrase",[phrase])

def handle_forward_ir(mqtt_sender, speed_entry, handle_forward_ir_entry):
    speed_entry=speed_entry.get()
    distance=handle_forward_ir_entry.get()
    mqtt_sender.send_message("go_forward_with_ir",[distance,speed_entry])

def handle_backward_ir(mqtt_sender, speed_entry, handle_backward_ir_entry):
    speed_entry=speed_entry.get()
    distance=handle_backward_ir_entry.get()
    mqtt_sender.send_message("go_backward_with_ir",[distance, speed_entry])

def handle_distance_ir(mqtt_sender,speed_entry, go_until_distance_with_ir_entry,delta_entry):
    delta=delta_entry.get()
    speed_entry=speed_entry.get()
    distance=go_until_distance_with_ir_entry.get()
    mqtt_sender.send_message("go until distance",[delta,distance, speed_entry])
