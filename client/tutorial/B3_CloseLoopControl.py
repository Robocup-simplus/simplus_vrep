"""
            B3 Close Loop Control! [Basic]

            Created on 2020.May.28

    Now That we received data and senc command successfully,
    It's time to make a closed loop program that repeat as below:
        1. Receive Data
        2. Decide What to Do
        3. Send Command
        4. Repeat!

    Hopefully we are on the async side of API so you don't have to deal with repeat step and managing loop speed.
    So, if we wrap up:
        1. Receive Data (We did it in step 1)
        2. Decide What to Do (We do it here) TODO(*)
        3. Send Command (We did it in step 2)
        4. Repeat! (We don't need to do it!)

    TODO:
        1. Fill the missing codes from last tutorials you complete
        2. Fill the control function and complete todos
        3. Call think funcion in right place of Play function
        4. Watch and Enjoy ! (You can play with parameter and numbers in code to find a better control)
"""
import client
from client.python.simplus_pb2 import *

info = WorldInfo()  # You can access world info everywhere


def Start(world_info, team_info):
    """ THIS FUNCTION WILL BE CALLED IN THE BEGINING
        world_info : IN  {team_count, robot_per_team, color_sensors, distance_sensors, check_points}
        team_info  : OUT {name}
    """
    global info
    info = world_info
    # TODO: Fill your team information
    # TODO: Replace below todo with 'your team name'
    team_info.name = TODO


def End(server, result):
    """ THIS FUNCTION WILL BE CALLED AT THE END
        server : IN server Infomation {time, score, state}
        result : OUT {message, map}
    """
    # Get ending server info from server

    # Fill your final result here
    # TODO: Fill the Ending Message
    # TODO: You can send 'Bye' when you want to quit or 'End' when you want the referee calculate and show your scores
    result.message = TODO


def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[], heatCamera}
        command    : OUT {linear, angular, LED, victims[]}
    """
    # Your code will be here
    # You get unique ID of our current robot in the field id
    # You can read data from observation and server
    # You should fill the command for your robots

    # In this practice we just trying to show that connection of simulator and your code is correct
    # TODO: Try fill this section from the code of last tutorial <B1>
    print('=====================================')
    print('Server Time is:', TODO)
    print('Your Score:', TODO)
    print('State of Server:', TODO)
    print('Position of Robot:', TODO)
    print('Color Sensors:', TODO)
    print('Distance Sensors:', TODO)
    print('hearCamera:', TODO)
    img = convert_to_cv_img(TODO, TODO, TODO)  # Find the function in below
    print('Camera Image shape:', TODO)  # Using OpenCV
    print('Camera Image size:', TODO)  # Using OpenCV
    print('Camera Image dtype:', TODO)  # Using OpenCV

    # TODO: call control function


""" Helper Function to conver raw image to OpenCV image"""
# Convert raw image to open cv image
import numpy as np
import cv2 as cv


# You should feed camera raw, camera height and camera width to this function to get OpenCV Image
def convert_to_cv_img(img_raw, h, w):
    img_array = np.frombuffer(img_raw, dtype=np.uint8)
    img = img_array.reshape(h, w, 3)
    img_center = (w / 2, h / 2)
    mirrored_img = cv.getRotationMatrix2D(img_center, 180.0, 1.0)
    main_img = cv.warpAffine(img, mirrored_img, (w, h))
    main_img = cv.flip(main_img, 1)
    return main_img


""" Helper Function to move the robot"""
# Convert text command to Robot Velocity Command


GO_FW = 'FORWARD'
GO_BW = 'BACKWARD'
TURN_LT = 'TURN_LEFT'
TURN_RT = 'TURN_RIGHT'
STOP = 'STOP'


# You should feed camera raw, camera height and camera width to this function to get OpenCV Image
# command: OUT {linear, angular, LED, victims[]}
def move_robot(text_commad):
    command = Command(id=1)
    if text_commad == 'FORWARD':
        command.linear = 0.1
        command.angular = 0.0
        command.LED = 'green'
    if text_commad == 'BACKWARD':
        command.linear = TODO  # Set a negative value to make robot go backward (See. Forward)
        command.angular = TODO  # Set the right value to make robot go backward (See. Forward)
        command.LED = TODO  # Make it green
    if text_commad == 'TURN_LEFT':
        command.linear = 0.0
        command.angular = 0.2
        command.LED = 'blue'
    if text_commad == 'TURN_RIGHT':
        command.linear = TODO  # Set the right value to make robot turn right (See. Turn Left)
        command.angular = TODO  # Set a negative value to make robot turn right (See. Turn Left)
        command.LED = TODO  # Make it blue
    if text_commad == 'STOP':
        command.linear = 0.0
        command.angular = 0.0
        command.LED = 'red'
    return command


PREV_TURN = STOP  # Store previous turn in this variable


def control(observation):
    sensivity = 10  # Higher number means robot more afraid of hitting obstacles
    detected_obstacle = []
    for i, sensor in enumerate(observation.distances):
        if sensor.detected == True and sensor.distance < 1 / sensivity:
            detected_obstacle.append(i)  # There is an obstacle near sensor number "i"

    # define sensor locations
    #
    #    Map of Sensor location on Robot
    #
    #           /--- *2* ---- *3* ---\
    #          /                      \
    #        *1*                      *4*
    #         |       SIMPLUS          |
    #        *0*        ROBOT         *5*
    #         |                        |
    #          \                      /
    #          *7* -----------------*6*
    #
    left_1 = 0
    left_2 = 1
    front_1 = 2
    front_2 = 3
    right_1 = 4
    right_2 = 5
    back_right = 6
    back_left = 7

    global PREV_TURN
    if front_1 not in detected_obstacle and front_2 not in detected_obstacle:  # FORWARD
        move_robot(GO_FW)
    elif left_1 not in detected_obstacle or left_2 not in detected_obstacle:
        move_robot(TURN_LT)
        PREV_TURN = TURN_LT
    elif right_1 not in detected_obstacle or right_2 not in detected_obstacle:
        move_robot(TURN_RT)
        PREV_TURN = TURN_RT
    elif back_right not in detected_obstacle:
        move_robot(TODO)  # Turn to Right
        PREV_TURN = TODO
    elif back_left not in detected_obstacle:
        move_robot(TODO)  # Turn to Left
        PREV_TURN = TODO
    else:
        move_robot(PREV_TURN)
