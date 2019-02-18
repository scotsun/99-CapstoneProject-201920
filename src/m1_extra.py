# This module contains the functions that will be imported to the share_gui_delegate module
import rosebot
import time
import math
import mqtt_remote_method_calls as com


def sprint3_forward(robot, left_speed, right_speed):
    '''
    :type robot rosebot.RoseBot
    '''
    # This function allows the "detector" to move forward and remove the obstacles on its pathway
    # In details, it will grab the object, turn by some degrees, and finally drop the objects
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(left_speed, right_speed)

    while True:
        distance_to_ob = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if distance_to_ob <= 10:
            robot.sound_system.beeper.beep()
            time.sleep(math.exp(-distance_to_ob+10))
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 5:
                robot.drive_system.stop()
                break


def sprint3_clear_path(robot):
    '''
    :type robot rosebot.RoseBot
    '''
    robot.arm_and_claw.raise_arm()
    start_time = time.time()
    robot.drive_system.go(-25, 25)
    while True:
        if time.time()-start_time >= 8:
            robot.drive_system.stop()
            robot.arm_and_claw.lower_arm()
            robot.sound_system.speak_phrase("Object is removed")
            break


def sprint3_detect(robot, mode):
    '''
    :type robot rosebot.RoseBot
    '''
    if mode == "Oil":
        if robot.sensor_system.color_sensor.get_color_as_name() == "Black": #TODO: might change the colors
            robot.sound_system.speak_phrase("I found Oil")
    if mode == "Metal":
        if robot.sensor_system.color_sensor.get_color_as_name() == "White":
            robot.sound_system.speak_phrase("I found Metal")


def roboprint(robot, mqtt_client):
    color = robot.sensor_system.color_sensor.get_color_as_name()
    if color == "Black":
        print("I found a source of oil :)")
        mqtt_client.send_message("help")
    elif color == "White":
        print("I found a source of metal :)")
    else:
        print("I found nothing :(")
