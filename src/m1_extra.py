# This module contains the functions that will be imported to the share_gui_delegate module
import rosebot

def m1_sprint3_forward(robot, left_speed, right_speed):
    '''
    :type robot rosebot.RoseBot
    '''
    # This function allows the "detector" to move forward and remove the obstacles on its pathway
    # In details, it will grab the object, turn by some degrees, and finally drop the objects
    robot.drive_system.go(left_speed, right_speed)
