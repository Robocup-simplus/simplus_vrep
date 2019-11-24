import client
from simplus_pb2 import *
import numpy as np

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

    col = ['red', 'green', 'blue', 'akldjf']
    a = [0, 0, 0]
    for c in observation.colors:
        a[0] += c.r
        a[1] += c.g
        a[2] += c.b
    command.LED = col[int(np.argmax(a))]
    obstacle = 0
    for i in range(1, 5):
        obstacle += observation.distances[i].detected

    if obstacle == 0:
        command.linear = 0.05
        command.angular = 0.0
    else:
        command.linear = 0.0
        command.angular = 0.5
    command.actions.append('salam', observation.pos.x, observation.pos.y, observation.pos.z)
