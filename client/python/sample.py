import client
from simplus_pb2 import *

info = WorldInfo() # You can access world info everywhere
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
        observation: IN {camera, position, color[], distance[], heatCamera}
        command    : OUT {linear, angular, LED, victims[]}
    """
    # Your will be here
    # Sample Code
    obstacle=0
    for i in range(8):
        obstacle+=observation.distances[0].distance
        print(observation.distances[0].detected,observation.distances[0].distance)

    if(obstacle==0):
        command.linear = 0.01
        command.angular = 0.0
    else:
        command.linear = 0.0
        command.angular = 0.1