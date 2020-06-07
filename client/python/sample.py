import client
from simplus_pb2 import *
import random
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


GO_FW = 'FORWARD'
GO_BW = 'BACKWARD'
TURN_LT = 'TURN_LEFT'
TURN_RT = 'TURN_RIGHT'
STOP = 'STOP'

last_turn = GO_FW
def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[], heatCamera}
        command    : OUT {linear, angular, LED, victims[]}
    """
    # Your will be here
    # Sample Code
    sensivity = 7  # Higher number means robot more afraid of hitting obstacles

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
    print('d', detected_obstacle)
    if 2 not in detected_obstacle and 3 not in detected_obstacle:  # If we can go forward we don't roll a dice
        command.linear, command.angular, command.LED = move_robot(GO_FW)
        last_turn = GO_FW
        return


    # forward is block to we should choose a way to turn (Left or Right)
    # but only if they have at least one free sensor who has more free holes has more chances too
    if last_turn == GO_FW:
        last_turn = random.sample([TURN_RT, TURN_LT], 1)[0]
        command.linear, command.angular, command.LED = move_robot(last_turn)
    else:
        command.linear, command.angular, command.LED = move_robot(last_turn)





def move_robot(text_commad):
    command = Command(id=0)
    if text_commad == 'FORWARD':
        command.linear = 0.05
        command.angular = 0.0
        command.LED = 'green'
    if text_commad == 'BACKWARD':
        command.linear = -0.1  # Set a negative value to make robot go backward (See. Forward)
        command.angular = 0.0  # Set the right value to make robot go backward (See. Forward)
        command.LED = 'green'  # Make it green
    if text_commad == 'TURN_LEFT':
        command.linear = 0.0
        command.angular = 0.2
        command.LED = 'blue'
    if text_commad == 'TURN_RIGHT':
        command.linear = 0.0  # Set the right value to make robot turn right (See. Turn Left)
        command.angular = -0.2  # Set a negative value to make robot turn right (See. Turn Left)
        command.LED = 'blue'  # Make it blue
    if text_commad == 'STOP':
        command.linear = 0.0
        command.angular = 0.0
        command.LED = 'red'
    return command.linear, command.angular, command.LED