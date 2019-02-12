# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
import rosebot
import math
import time
from rosebot import Motor

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
