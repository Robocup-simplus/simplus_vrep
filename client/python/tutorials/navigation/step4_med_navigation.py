import client
from simplus_pb2 import *
import numpy as np
import time


#### considering holes #####

    
info = WorldInfo()  # You can access world info everywhere


def control(observation):
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


        ########## hole detection
        is_black_center = False
        is_black_left = False    
        is_black_right = False
        sum_center = (observation.colors[0].r + observation.colors[0].g + observation.colors[0].b) 
        if ( sum_center >5 and sum_center<30):
            is_black_center = True  

        sum_left= (observation.colors[1].r + observation.colors[1].g + observation.colors[1].b) 
        if ( sum_left >5 and sum_left<30):
            is_black_left = True  

        sum_right= (observation.colors[2].r + observation.colors[2].g + observation.colors[2].b) 
        if ( sum_right >5 and sum_right<30):
            is_black_right = True  

        ########### decide #########

        if front_1 not in detected_obstacle and front_2 not in detected_obstacle and not is_black_center:  # FORWARD
            return 'FORWARD'
        elif (left_1 not in detected_obstacle or left_2 not in detected_obstacle) and not  is_black_left:
            direction = 'TURN_LEFT'
        elif (right_1 not in detected_obstacle or right_2 not in detected_obstacle) and not is_black_right:
            direction = 'TURN_RIGHT'
        elif back_right not in detected_obstacle:
            direction = 'TURN_RIGHT'
        elif back_left not in detected_obstacle:
            direction = 'TURN_LEFT'
        else:
            direction = PRE_MOVE
        PRE_MOVE = direction

        return direction;


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




PRE_MOVE = 'STOP'  # Store previous turn in this variable

def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """


    direction = control(observation) 

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
    