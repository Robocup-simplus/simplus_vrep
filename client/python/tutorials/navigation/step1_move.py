"""
    Move IT! [Basic]
    Created on 2020.May.28
    A review of connection flows:
    This is the flow of connections
     +------------  Syncronous Connections --------------><------------  Asyncronous Connections ------------+
    V-REP ------- vrep_api<observations_data> ------> Server ---------- grpc<observation> ----------> Clients
    V-REP <------ vrep_api<command_to_robots> ------- Server <--------- grpc<commands> -------------- Clients
    For simplicity of connection we add one more logical layer over Client to hide the grpc and network complexity.
    In This file we continue the last tutorial by going one step further and move the robot.
    For your practice, some part of code left empty to be filled
    after using this file robot should move forward and then start to turn around itself.
"""
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
    # TODO: Fill your team information
    # TODO: Replace below todo with 'your team name'
    team_info.name = "Dragon"


def End(server, result):
    """ THIS FUNCTION WILL BE CALLED AT THE END
        server : IN server Infomation {time, score, state}
        result : OUT {message, map}
    """
    # Get ending server info from server

    # Fill your final result here
    # TODO: Fill the Ending Message
    # TODO: You can send 'Bye' when you want to quit or 'End' when you want the referee calculate and show your scores
    result.message = "It was a great game"


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


    # TODO: In This tutorial we want to make robot do below instruction:
    #   1. Go Forward for 20 cycle
    #   2. Turn Left for 10 cycle
    #   3. Go Forward for 20 cycle
    #   4. Turn Right for 10 cycle
    #   5. Go Forward for 20 cycle
    #   5. Go Backward for 10 cycle
    #   6. Go Backward for 10 cycle
    #   7.  random
    #   8. Have Fun with playing with robot and changing LED colors :)

    direction=''
    if server.time < 20:
        direction = 'FORWARD' # Make Robot Go forward for 20 cycle
    elif server.time < 20 + 10:
        direction = 'TURN_LEFT'  # Make Robot Turn left for 10 cycle
    elif server.time < 20 + 10 + 20:
        direction = 'FORWARD'  # Go forward
    elif server.time < 20 + 10 + 20 + 10 + 10:
        direction = 'TURN_RIGHT'  # Fill To Turn Right
    elif server.time < 20 + 10 + 20 + 10 + 10 + 10:
        direction = 'FORWARD'  # Go Forward
    elif server.time < 20 + 10 + 20 + 10 + 10 + 20 + 10:
        direction = 'BACKWARD'  # Fill To Go Backward
    elif server.time < 20 + 10 + 20 + 10 + 10 + 20 + 10 + 10:
        direction = 'STOP'  # Fill To Stop
    elif server.time %10  < 4: # 3 step
        direction = 'TURN_LEFT' 
    else:
        direction = 'FORWARD' 


    if direction == 'FORWARD':
        command.linear =  0.1
        command.angular = 0.0
        command.LED = 'green'
    if direction == 'BACKWARD':
        command.linear = -0.1 # Set a negative value to make robot go backward (See. Forward)
        command.angular = 0.0 # Set the 0 value to make robot go backward (See. Forward)
        command.LED = 'green' # Make it green
    if direction == 'TURN_LEFT':
        command.linear = 0.0
        command.angular = 0.3
        command.LED = 'blue'
    if direction == 'TURN_RIGHT':
        command.linear = 0.0 # Set the 0 value to make robot turn right (See. Turn Left)
        command.angular = -0.3  # Set a negative value to make robot turn right (See. Turn Left)
        command.LED = 'blue' # Make it blue
    if direction == 'STOP':
        command.linear = 0.0
        command.angular = 0.0
        command.LED = 'red'
