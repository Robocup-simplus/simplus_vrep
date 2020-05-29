import client
from simplus_pb2 import *

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

last_turn = 0.1
def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[], heatCamera}
        command    : OUT {linear, angular, LED, victims[]}
    """
    # Your will be here
    # Sample Code
    obstacle = 0
    for i in range(8):
        obstacle += observation.distances[i].distance
        print(i, observation.distances[i].detected, observation.distances[i].distance)
    obs = [i for i, d in enumerate(observation.distances) if d.detected and d.distance < 0.1]
    global last_turn
    if 2 not in obs and 3 not in obs:  # FORWARD
        command.linear = 0.05
        command.angular = 0.0
        command.LED = 'green'
    elif 0 not in obs or 1 not in obs:
        command.linear = 0.0
        last_turn = command.angular = 0.2
        command.LED = 'blue'
    elif 5 not in obs or 4 not in obs:
        command.linear = 0.0
        last_turn = command.angular = -0.2
        command.LED = 'blue'
    elif 7 not in obs or 6 not in obs:
        command.linear = 0.0
        command.angular = last_turn
        command.LED = 'blue'
    else:
        command.linear = 0.0
        command.angular = last_turn
        command.LED = 'red'
