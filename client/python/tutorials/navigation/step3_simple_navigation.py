import client
from simplus_pb2 import *
import numpy as np
import time
import random


#     This inspirational quote, is actually our core idea for solving maze in this tutorial.
#     As we want to cover all map we want to go to everywhere we never been,
#     and for make sure that we are taking new paths, we should keep track of place that we've been before.(next tutorial)
#     OR
#     we can select random action anytime we face a dilemma.
#     in this case our action are left or right so we have 50% chance,
#     to make the good decision with no effort of hard thinking.

    
info = WorldInfo()  # You can access world info everywhere



def Start(world_info, team_info):
    """ THIS FUNCTION WILL BE CALLED IN THE BEGINING
        world_info : IN  {team_count, robot_per_team, color_sensors, distance_sensors, check_points}
        team_info  : OUT {name}
    """
    global info
    info = world_info
    # Fill your team information
    team_info.name = 'Dragon'


def End(server, result):
    """ THIS FUNCTION WILL BE CALLED AT THE END
        server : IN server Infomation {time, score, state}
        result : OUT {message, map}
    """
    # Get ending server info from server

    # Fill your final result here

    result.message = 'Good game!'



def control_v1(observation):

        # Working with proximity sensor

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

        sensivity = 10  # Higher number means robot more afraid of hitting obstacles
        detected_obstacle = []
        for i, sensor in enumerate(observation.distances):
            if sensor.detected == True and sensor.distance < 1 / sensivity:
                detected_obstacle.append(i)  # There is an obstacle near sensor number "i"

        left_1 = 0
        left_2 = 1
        front_1 = 2
        front_2 = 3
        right_1 = 4
        right_2 = 5
        back_right = 6
        back_left = 7

        global PRE_MOVE
        direction=''

        if front_1 not in detected_obstacle and front_2 not in detected_obstacle:  # FORWARD
            return 'FORWARD'
        elif left_1 not in detected_obstacle or left_2 not in detected_obstacle:
            direction = 'TURN_LEFT'
        elif right_1 not in detected_obstacle or right_2 not in detected_obstacle:
            direction = 'TURN_RIGHT'
        elif back_right not in detected_obstacle:
            direction = 'TURN_RIGHT'
        elif back_left not in detected_obstacle:
            direction = 'TURN_LEFT'
        else:
            direction = PRE_MOVE
        PRE_MOVE = direction

        return direction;


def control_v2(observation):
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
        last_turn = 'FORWARD'
        return 'FORWARD'

    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    if last_turn == 'FORWARD':
        last_turn = random.sample(['TURN_RIGHT', 'TURN_LEFT'], 1)[0]
        return last_turn
    else:
        return last_turn


PRE_MOVE = 'STOP'  # Store previous turn in this variable

def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """

    

    # Working with Color Sensor and LED

    a = [0, 0, 0] #[r,g,b]
    for c in observation.colors:
        a[0] += c.r
        a[1] += c.g
        a[2] += c.b

    if a[0]> a[1] and a[0]>a[2]:
        command.LED = 'red'
    elif a[1]> a[0] and a[1]>a[0]:

        command.LED = 'green'
    else:
        command.LED = 'blue'


    direction = control_v1(observation) 

    if direction == 'FORWARD':
        command.linear =  0.1
        command.angular = 0.0
    if direction == 'BACKWARD':
        command.linear = -0.1 # Set a negative value to make robot go backward (See. Forward)
        command.angular = 0.0 # Set the 0 value to make robot go backward (See. Forward)
    if direction == 'TURN_LEFT':
        command.linear = 0.0
        command.angular = 0.3
    if direction == 'TURN_RIGHT':
        command.linear = 0.0 # Set the 0 value to make robot turn right (See. Turn Left)
        command.angular = -0.3  # Set a negative value to make robot turn right (See. Turn Left)
    if direction == 'STOP':
        command.linear = 0.0
        command.angular = 0.0




    
    

    