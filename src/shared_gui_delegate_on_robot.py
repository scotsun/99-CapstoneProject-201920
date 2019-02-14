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
        self.is_time_to_stop=False

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

    def quit(self):
        self.is_time_to_stop = True

    def exit(self):
        print('exit')


    def go_straight_using_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(seconds, speed)

    def go_for_inches_w_time_approach(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(inches, speed)

    def go_for_inches_encoder_approach(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, speed)

    def beep_n_times(self, number_of_beeps):
        self.robot.sound_system.beep_for_n_times(number_of_beeps)

    def play_frequency_for_duration(self, frequency, duration):
        self.robot.sound_system.tone_freq(frequency, duration)

    def speak_phrase(self, phrase):
        phrase=str(phrase)
        self.robot.sound_system.speak_phrase(phrase)

    def go_forward_with_ir(self,distance,speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(distance,speed)
    def go_backward_with_ir(self,distance,speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(distance,speed)
    def go_until_distance(self,delta,distance,speed):
        self.robot.drive_system.go_until_distance_is_within(delta,distance,speed)

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity, speed)

    def go_straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, speed)

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, speed)

    def display_camera_data(self):
        self.robot.drive_system.display_camera_date()

    def spin_clockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))


    def m1_Go_with_IR_and_beeps(self, inches, speed, rate):
        import time
        self.robot.drive_system.go(speed, speed)
        while True:
            for i in range(rate):
                self.robot.sound_system.beeper.beep()
                time.sleep(0.1)
            rate += 1
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= inches:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break




    def m2_Go_with_IR_and_tones(self,freq,speed,rate):
        import time
        freq=int(freq)
        speed=int(speed)
        rate=int(rate)
        distance=5
        self.robot.arm_and_claw.lower_arm()
        c=self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if c<distance:
            self.stop()
        else:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<distance:
                self.stop()
            else:
                self.robot.drive_system.go(speed,speed)
        k=1
        time.sleep(0.1)
        diff=0.1
        while True:
            t=self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            t1=self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            self.robot.sound_system.tone_freq(freq+rate*(c-t1),10)
            if abs(t-t1)<diff:
                if t1<distance:
                    self.stop()
                    break
        self.robot.arm_and_claw.move_arm_to_position(2000)
        self.robot.arm_and_claw.move_arm_to_position(5000)
        time.sleep(2)




    def m2_Spin_and_grab(self,direction,speed,freq,rate):
        if direction=='clockwise':
            self.robot.drive_system.spin_clockwise_until_sees_object(speed,25)
        else:
            self.robot.drive_system.spin_counterclockwise_until_sees_object(speed,25)
        self.m2_Go_with_IR_and_tones(freq,rate,speed)
    def P_of_PID_control(self,speed):
        original=self.robot.sensor_system.color_system.get_reflected_light_intensity()
        for k in range(5):
            current=self.robot.sensor_system.color_system.get_reflected_light_intensity()
            error=current-original
            self.robot.drive_system.go(B+(error*K1),B+(error*K2))