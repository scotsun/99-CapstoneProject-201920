# This module contains the functions that will be imported to the share_gui_delegate module
import rosebot
import time


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
        if distance_to_ob <= 15:
            robot.sound_system.beeper.beep()
            time.sleep((distance_to_ob**0.5)/10)
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
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
        if time.time()-start_time >= 3:
            robot.drive_system.stop()
            robot.arm_and_claw.lower_arm()
            robot.sound_system.speak_phrase("Object is removed")
            break




def sprint3_detect(robot, mode, mqtt_client):
    '''
    :type robot rosebot.RoseBot
    '''
    color = robot.sensor_system.color_sensor.get_color_as_name()
    if mode == "Oil" and color == "Black":
        robot.sound_system.speak_phrase("I found Oil")
        message = 1
    elif mode == "Metal" and color == "White":
        robot.sound_system.speak_phrase("I found Metal")
        message = 2
    else:
        robot.sound_system.speak_phrase("I found nothing")
        message = 3
    mqtt_client.send_message("roboprint", [message])
