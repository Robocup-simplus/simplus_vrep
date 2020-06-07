"""
            C1 Solving Maze! [Basic]

            Created on 2020.May.29

   We see how to control robots for a simple objective,
   (like moving forward and not to hit obstacles) in B3.

   Now we want so write controller for a harder objective. Solving the Maze!

   In this practice we use and intiutive and naive approuch for solving maze, and
   in next tutorial we see A* an optimum  algorithm for solving maze

    We are working on the final result of the last tutorial, so make sure you complete B3 before starting A1.

        `If you want to go somewhere you never been, You should take paths that you never takes`
    This inspirational quote, is actually our core idea for solving maze in this tutorial.
    As we want to cover all map we want to go to everywhere we never been,
    and for make sure that we are taking new paths, we should keep track of place that we've been before.(next tutorial)
    OR
    we can select random action anytime we face a dilemma.
    in this case our action are left or right so we have 50% chance,
    to make the good decision with no effort of hard thinking.

    TODO:
        1. Fill the missing codes from last tutorials you complete
        2. Fill the monte_carlo_control function and complete todos (Random Only)
        3. Watch and Enjoy ! (You can play with parameter and numbers in code to find a better control)
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

    # TODO: 1. call monte carlo control function
    # TODO: 2. call never look back control function
    command = TODO

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
    command = Command(id=0)
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
        return move_robot(GO_FW)
    elif left_1 not in detected_obstacle or left_2 not in detected_obstacle:
        PREV_TURN = TURN_LT
        return move_robot(TURN_LT)
    elif right_1 not in detected_obstacle or right_2 not in detected_obstacle:
        PREV_TURN = TURN_RT
        return move_robot(TURN_RT)
    elif back_right not in detected_obstacle:
        PREV_TURN = TODO
        return move_robot(TODO)  # Turn to Right
    elif back_left not in detected_obstacle:
        PREV_TURN = TODO
        return move_robot(TODO)  # Turn to Left
    else:
        return move_robot(PREV_TURN)


import random


def monte_carlo_control(observation):
    sensivity = 10  # Higher number means robot more afraid of hitting obstacles

    # Detect Obstacles
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

    global last_turn

    forward_free = 2.5
    if 2 not in detected_obstacle and 3 not in detected_obstacle: # If we can go forward we don't roll a dice
        last_turn = GO_FW
        return move_robot(GO_FW)

    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    if last_turn == GO_FW:
        last_turn = random.sample([TURN_RT, TURN_LT], 1)[0]
        return move_robot(last_turn)
    else:
        return move_robot(last_turn)


def never_look_back_control(observation):
    sensivity = 10  # Higher number means robot more afraid of hitting obstacles

    # Detect Obstacles
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

    global last_turn

    forward_free = 2.5
    if 2 not in detected_obstacle and 3 not in detected_obstacle: # If we can go forward we don't roll a dice
        last_turn = GO_FW
        return move_robot(GO_FW)
    else:
        sum
    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    if last_turn == GO_FW:
        last_turn = random.sample([TURN_RT, TURN_LT], 1)[0]
        return move_robot(last_turn)
    else:
        return move_robot(last_turn)
