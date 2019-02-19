import rosebot
import time


def idle_animation(self, speed, area):
    speed = int(speed)
    area = int(area)
    while True:
        start = time.time()
        while True:
            time.sleep(0.5)
            current_height = self.sensor_system.camera.get_biggest_blob().height
            current_width = self.sensor_system.camera.get_biggest_blob().width
            current_area = current_height * current_width
            self.drive_system.go(-speed, speed)
            if current_area > area:
                self.drive_system.stop()
                break
            elif abs(time.time() - start) > 5:
                self.drive_system.stop()
                break
        if current_area > area:
            print('stopping')
            self.drive_system.stop()
            break
        start=time.time()
        while True:
            time.sleep(0.2)
            current_height = self.sensor_system.camera.get_biggest_blob().height
            current_width = self.sensor_system.camera.get_biggest_blob().width
            current_area = current_height * current_width
            self.drive_system.go(speed, -speed)
            if current_area > area:
                self.drive_system.stop()
                break
            elif abs(time.time() - start) > 5:
                self.drive_system.stop()
                break
        if current_area > area:
            print('stopping')
            self.drive_system.stop()
            break


def determine_location(self):
    if self.sensor_system.camera.get_biggest_blob().is_against_left_edge() == True:
        return ('left')
    elif self.sensor_system.camera.get_biggest_blob().is_against_right_edge() == True:
        return ('right')
    else:
        return ('Unknown')


def go_to_object_left(self, speed,distance):
    distance=int(distance)
    speed = int(speed)
    self.drive_system.go(speed, speed)
    while True:
        while True:
            if self.sensor_system.camera.get_biggest_blob().get_area() < 1:
                self.drive_system.stop()
                break
            elif self.sensor_system.ir_proximity_sensor.get_distance_in_inches() < distance:
                self.drive_system.stop()
                break
        self.drive_system.spin_counterclockwise_until_sees_object(25, 25)
        t = self.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        t1 = self.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if (t - t1) < 0.1:
            break


def go_to_object_right(self, speed,distance):
    distance=int(distance)
    speed = int(speed)
    self.drive_system.go(speed, speed)
    while True:
        while True:
            if self.sensor_system.camera.get_biggest_blob().get_area() < 1:
                self.drive_system.stop()
                break
            elif self.sensor_system.ir_proximity_sensor.get_distance_in_inches() < distance:
                self.drive_system.stop()
                break
        self.drive_system.spin_clockwise_until_sees_object(25, 25)
        t = self.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        t1 = self.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if (t - t1) < 0.1:
            break

def fist_bump(self):
    #Robot must be 15 inches away
    self.arm_and_claw.lower_arm()
    self.drive_system.go_straight_for_inches_using_time(15,25)
    self.sound_system.speak_phrase('yay')
    time.sleep(1)
    self.drive_system.stop()
    self.drive_system.go(-50,-50)
    time.sleep(4)
    self.drive_system.go(100,-100)
    time.sleep(1.5)
    self.drive_system.stop()
    self.drive_system.go_straight_for_inches_using_time(15,80)

def sleep_animation(self):
    self.led_system.left_led.turn_on()
    self.led_system.right_led.turn_on()
    brightness=1
    for k in range(9):
        self.led_system.left_led.set_color_by_fractions(0,brightness)
        self.led_system.right_led.set_color_by_fractions(0, brightness)
        brightness=brightness-0.1
        time.sleep(1)
    self.sound_system.speak_phrase('sleep time')
    time.sleep(1)
    self.led_system.left_led.turn_off()
    self.led_system.right_led.turn_off()
