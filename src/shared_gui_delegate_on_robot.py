"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Emily Wilcox, Scott Sun, Daniel Pollack.
  Winter term, 2018-2019.
"""
import rosebot

class DelegateThatReceives(object):
    def __init__(self, robot):
        """
        :type robot: rosebot.Rosebot
        """
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), -int(right_wheel_speed))

    def stop(self):
        self.robot.drive_system.stop()

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()
    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()
    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()
    def move_arm_to_position(self,arm_position):
        self.robot.arm_and_claw.move_arm_to_position(arm_position)

