# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

import math
import time
from rosebot import Motor
from rosebot import SensorSystem
from rosebot import Camera
from rosebot import Blob
import tkinter
from tkinter import ttk

class DS(object):
    """
        Controls the robot's motion via GO and STOP methods,
            along with various methods that GO/STOP under control of a sensor.
        """

    # -------------------------------------------------------------------------
    # NOTE:
    #   Throughout, when going straight:
    #     -- Positive speeds should make the robot move forward.
    #     -- Negative speeds should make the robot move backward.
    #   Throughout, when spinning:
    #     -- Positive speeds should make the robot spin in place clockwise
    #          (i.e., left motor goes at speed S, right motor at speed -S).
    #     -- Negative speeds should make the robot spin in place
    #          counter-clockwise
    #          (i.e., left motor goes at speed -S, right motor at speed S).
    # -------------------------------------------------------------------------

    def __init__(self, sensor_system):
        """
        Stores the given SensorSystem object.
        Constructs two Motors (for the left and right wheels).
          :type sensor_system:  SensorSystem
        """
        self.sensor_system = sensor_system
        self.left_motor = Motor('B')
        self.right_motor = Motor('C')

        self.wheel_circumference = 1.3 * math.pi

    # -------------------------------------------------------------------------
    # Methods for driving with no external sensor (just the built-in encoders).
    # -------------------------------------------------------------------------

    def go(self, left_wheel_speed, right_wheel_speed):
        """ Makes the left and right wheel motors spin at the given speeds. """
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)

    def stop(self):
        self.left_motor.turn_off()
        self.right_motor.turn_off()
        """ Stops the left and right wheel motors. """

    def go_straight_for_seconds(self, seconds, speed):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        at the given speed for the given number of seconds.
        """
        start = time.time()
        self.go(speed, speed)

        while True:
            if time.time() - start >= seconds:
                self.stop()
                break

    def go_straight_for_inches_using_time(self, inches, speed):
        """
        Makes the robot go straight at the given speed
        for the given number of inches, using the approximate
        conversion factor of 10.0 inches per second at 100 (full) speed.
        """

        seconds_per_inch_at_100 = 10.0  # 1 sec = 10 inches at 100 speed
        seconds = abs(inches * seconds_per_inch_at_100 / speed)

        self.go_straight_for_seconds(seconds, speed)

    def go_straight_for_inches_using_encoder(self, inches, speed):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        at the given speed for the given number of inches,
        using the encoder (degrees traveled sensor) built into the motors.
        """
        inches_per_degree = 1.3 * math.pi / 360
        stop_position = inches / inches_per_degree

        self.left_motor.reset_position()
        self.go(speed, speed)
        while True:
            current_position = self.left_motor.get_position()
            if abs(current_position) >= abs(stop_position):
                self.stop()
                break

    # -------------------------------------------------------------------------
    # Methods for driving that use the color sensor.
    # -------------------------------------------------------------------------

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        """
        Goes straight at the given speed until the intensity returned
        by the color_sensor is less than the given intensity.
        """
        self.go(speed, speed)
        while True:
            current_intensity = self.sensor_system.color_sensor.get_reflected_light_intensity()
            if current_intensity < intensity:
                self.stop()
                break

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        """
        Goes straight at the given speed until the intensity returned
        by the color_sensor is greater than the given intensity.
        """
        self.go(speed, speed)
        while True:
            current_intensity = self.sensor_system.color_sensor.get_reflected_light_intensity()
            if current_intensity > intensity:
                self.stop()
                break

    def go_straight_until_color_is(self, color, speed):
        """
        Goes straight at the given speed until the color returned
        by the color_sensor is equal to the given color.

        Colors can be integers from 0 to 7 or any of the strings
        listed in the ColorSensor class.

        If the color is an integer (int), then use the  get_color   method
        to access the color sensor's color.  If the color is a string (str),
        then use the   get_color_as_name   method to access
        the color sensor's color.
        """
        self.go(speed, speed)
        if type(color) == int:
            while True:
                if self.sensor_system.color_sensor.get_color() == color:
                    self.stop()
                    break
        elif type(color) == str:
            while True:
                if self.sensor_system.color_sensor.get_color_as_name() == color:
                    self.stop()
                    break

    def go_straight_until_color_is_not(self, color, speed):
        """
        Goes straight at the given speed until the color returned
        by the color_sensor is NOT equal to the given color.

        Colors can be integers from 0 to 7 or any of the strings
        listed in the ColorSensor class.
        """
        self.go(speed, speed)
        if type(color) == int:
            while True:
                if self.sensor_system.color_sensor.get_color() != color:
                    self.stop()
                    break
        elif type(color) == str:
            while True:
                if self.sensor_system.color_sensor.get_color_as_name() != color:
                    self.stop()
                    break

    # -------------------------------------------------------------------------
    # Methods for driving that use the camera.
    # -------------------------------------------------------------------------
    def display_camera_data(self):
        """
        Prints on the Console the Blob data of the Blob that the camera sees
        (if any).
        """
        print(self.sensor_system.camera.get_biggest_blob())

    def spin_clockwise_until_sees_object(self, speed, area):
        """
        Spins clockwise at the given speed until the camera sees an object
        of the trained color whose area is at least the given area.
        Requires that the user train the camera on the color of the object.
        """
        while True:
            current_height = self.sensor_system.camera.get_biggest_blob().height
            current_width = self.sensor_system.camera.get_biggest_blob().width
            current_area = current_height * current_width

            if current_area != area:
                self.go(speed, -speed)
                time.sleep(0.2)
                self.stop()
            else:
                break

    def spin_counterclockwise_until_sees_object(self, speed, area):
        """
        Spins counter-clockwise at the given speed until the camera sees an object
        of the trained color whose area is at least the given area.
        Requires that the user train the camera on the color of the object.
        """

        while True:
            current_height = self.sensor_system.camera.get_biggest_blob().height
            current_width = self.sensor_system.camera.get_biggest_blob().width
            current_area = current_height * current_width

            if current_area != area:
                self.go(-speed, speed)
                time.sleep(0.2)
                self.stop()
            else:
                break


# shared gui
def get_ColorSensor_driving_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    intensity_label = ttk.Label(frame, text="Intensity")
    color_label = ttk.Label(frame, text="Color")
    speed_label = ttk.Label(frame, text="Speed")

    intensity_entry = ttk.Entry(frame, width=8)
    color_entry = ttk.Entry(frame, width=8)
    speed_entry = ttk.Entry(frame, width=8)

    go_straight_until_intensity_is_less_than_button = ttk.Button(frame,
                                                                 text="Go 'til In is less")
    go_straight_until_intensity_is_greater_than_button = ttk.Button(frame,
                                                                    text="Go 'til In is greater")
    go_straight_until_color_is_button = ttk.Button(frame,
                                                   text="Go 'til color")
    go_straight_until_color_is_not_button = ttk.Button(frame,
                                                       text="Go 'til Not color")

    intensity_label.grid(row=0, column=0)
    color_label.grid(row=0, column=2)
    speed_label.grid(row=0, column=4)
    intensity_entry.grid(row=1, column=0)
    color_entry.grid(row=1, column=2)
    speed_entry.grid(row=1, column=4)
    go_straight_until_intensity_is_less_than_button.grid(row=2, column=1)
    go_straight_until_intensity_is_greater_than_button.grid(row=2, column=3)
    go_straight_until_color_is_button.grid(row=3, column=1)
    go_straight_until_color_is_not_button.grid(row=3, column=3)

    # set button callbacks
    go_straight_until_intensity_is_less_than_button["command"] = lambda: (
        handler_go_straight_until_intensity_is_less_than_button(intensity_entry, speed_entry, mqtt_sender)
    )
    go_straight_until_intensity_is_greater_than_button["command"] = lambda: (
        handler_go_straight_until_intensity_is_greater_than_button(intensity_entry, speed_entry, mqtt_sender)
    )
    go_straight_until_color_is_button["command"] = lambda: (
        handler_go_straight_until_color_is_button(color_entry, speed_entry, mqtt_sender)
    )
    go_straight_until_color_is_not_button["command"] = lambda: (
        handler_go_straight_until_color_is_not_button(color_entry, speed_entry, mqtt_sender)
    )
    return frame

# Handlers
def handler_go_straight_until_intensity_is_less_than_button(intensity_entry, speed_entry, mqtt_sender):
    intensity = int(intensity_entry.get())
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_less_than", [intensity, speed])


def handler_go_straight_until_intensity_is_greater_than_button(intensity_entry, speed_entry, mqtt_sender):
    intensity = int(intensity_entry.get())
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_greater_than", [intensity, speed])


def handler_go_straight_until_color_is_button(color_entry, speed_entry, mqtt_sender):
    if len(color_entry.get()) == 1:
        color = int(color_entry.get())
    else:
        color = color_entry.get()
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_straight_until_color_is", [color, speed])


def handler_go_straight_until_color_is_not_button(color_entry, speed_entry, mqtt_sender):
    if len(color_entry.get()) == 1:
        color = int(color_entry.get())
    else:
        color = color_entry.get()
    speed = int(speed_entry.get())
    mqtt_sender.send_message("go_straight_until_color_is_not", [color, speed])



# Delegate class
class DelegateThatReceives(object):
    def __init__(self, robot):
        """
        :type robot: rosebot.Rosebot
        """
        self.robot = robot
        self.is_time_to_stop=False

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_great_than(intensity, speed)

    def go_straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, speed)

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, speed)
