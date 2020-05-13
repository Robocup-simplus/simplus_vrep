import client
from simplus_pb2 import *
import numpy as np
#import cv2 as cv
info = WorldInfo()  # You can access world info everywhere


def Start(world_info, team_info):
    """ THIS FUNCTION WILL BE CALLED IN THE BEGINING
        world_info : IN  {team_count, robot_per_team, color_sensors, distance_sensors, check_points}
        team_info  : OUT {name}
    """
    global info
    info = world_info
    # Fill your team information
    team_info.name = 'my_team_name'


def End(server, result):
    """ THIS FUNCTION WILL BE CALLED AT THE END
        server : IN server Infomation {time, score, state}
        result : OUT {message, map}
    """
    # Get ending server info from server

    # Fill your final result here
    result.message = 'The Ending Message'

import time
# testtime=time.time_ns()

def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """
    # for i, d in enumerate(observation.distances):
    #     print('DIS:', i, d.detected, d.distance)
    #
    # for i, c in enumerate(observation.colors):
    #     print('COL:', i, c.r, c.g, c.b)
    global testtime
    #print("dif time =",1000000000/(time.time_ns()-testtime))
    # testtime=time.time_ns()
    col = ['red', 'green', 'blue', 'akldjf']
    a = [0, 0, 0]
    for c in observation.colors:
        a[0] += c.r
        a[1] += c.g
        a[2] += c.b
    command.LED = col[int(np.argmax(a))]
    is_obstacle_left = False
    is_obstacle_right = False
    is_obstacle_Front = False


    if (observation.distances[1].detected==1 and observation.distances[1].distance<0.3) or (observation.distances[2].detected==1 and observation.distances[2].distance<0.3) :
        is_obstacle_left =True

    if (observation.distances[1].detected==1 and observation.distances[1].distance<0.3):
         is_obstacle_Front=True
    
    if (observation.distances[4].detected==1 and observation.distances[4].distance<0.3) or (observation.distances[5].detected==1 and observation.distances[5].distance<0.3):
        is_obstacle_right =True


    if not is_obstacle_left and not is_obstacle_Front and not is_obstacle_right:
        command.linear = 0.05
        command.angular = 0.0
    elif  is_obstacle_left and  is_obstacle_Front and  is_obstacle_right:
        command.linear = 0.0
        command.angular = 1
    elif is_obstacle_Front or is_obstacle_left:
        command.linear = 0.0
        command.angular = -0.5
    elif is_obstacle_right:
        command.linear = 0.0
        command.angular = 0.5
    
    for c in observation.colors:
       if(c.r>100 and c.r<215 and c.g<215 and c.b<215 and abs(int(c.r)-int(c.g))<45 and abs(int(c.g)-int(c.b))<45 and  abs(int(c.r)-int(c.b))<45 ):
           command.actions.append(Action(x=observation.pos.x,y=observation.pos.y,z=observation.pos.z,type='find_checkpoint'))
           break

    