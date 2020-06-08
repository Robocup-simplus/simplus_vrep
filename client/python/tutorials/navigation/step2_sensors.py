import client
from simplus_pb2 import *
import numpy as np
import time


#   We see how to control robots for a simple objective,
#    (like moving forward and not to hit obstacles) in here.
#    Now we want so write controller for a harder objective. Solving the Maze!
#    In this practice we use and intiutive and naive approuch for solving maze, and
#    in next tutorial we see A* an optimum  algorithm for solving maze


    

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




PRE_MOVE='FORWARD';

def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """

    global PRE_MOVE
    
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



    #move strategy   
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

    ############### check proximity sensor's status ################
    is_obstacle_left = False
    is_obstacle_right = False
    is_obstacle_Front = False

    sensivity = 10  # Higher number means robot more afraid of hitting obstacles
    min_dist= 1/sensivity

    if (observation.distances[3].detected and observation.distances[3].distance<min_dist) or (observation.distances[2].detected and observation.distances[2].distance<min_dist):
         is_obstacle_Front=True
    

    if (observation.distances[1].detected and observation.distances[1].distance<min_dist) or (observation.distances[0].detected and observation.distances[0].distance<min_dist) :
        is_obstacle_left =True


    if (observation.distances[4].detected and observation.distances[4].distance<min_dist) or (observation.distances[5].detected and observation.distances[5].distance<min_dist) :
        is_obstacle_right =True


    ############# Decide ###################
    if not is_obstacle_Front :
        direction='FORWARD'

    elif not is_obstacle_left :  #turn right
        direction='TURN_LEFT'

    elif not is_obstacle_right :   # turn left
        direction='TURN_RIGHT'

    elif  is_obstacle_left and  is_obstacle_Front and  is_obstacle_right:
        direction='BACKWARD'

    elif server.time %10  < 4: # 3 step
        direction='TURN_LEFT'
        
    else: # forward
        direction='FORWARD'
  
    PRE_MOVE = direction

    ############### move to direction ##################

    if direction == 'FORWARD':
        command.linear =  0.1
        command.angular = 0.0
    if direction == 'BACKWARD':
        command.linear = -0.1 # Set a negative value to make robot go backward (See. Forward)
        command.angular = 0.0 # Set the 0 value to make robot go backward (See. Forward)
    if direction == 'TURN_LEFT':
        command.linear = 0.0
        command.angular = 0.5
    if direction == 'TURN_RIGHT':
        command.linear = 0.0 # Set the 0 value to make robot turn right (See. Turn Left)
        command.angular = -0.5  # Set a negative value to make robot turn right (See. Turn Left)
    if direction == 'STOP':
        command.linear = 0.0
        command.angular = 0.0
  
    