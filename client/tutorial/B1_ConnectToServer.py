"""
            B1 Connecting to Server [Basic]

            Created on 2020.May.28

    This is the flow of connections

    +------------  Syncronous Connections --------------><------------  Asyncronous Connections ------------+

    V-REP ------- vrep_api<observations_data> ------> Server ---------- grpc<observation> ----------> Clients
    V-REP <------ vrep_api<command_to_robots> ------- Server <--------- grpc<commands> -------------- Clients

    For simplicity of connection we add one more logical layer over Client to hide the grpc and network complexity.

    So as a player of this league you only need to copy sample.py and fill the functions.
    The go to client.py and as mentioned there replace your module with the current player module. (See. TODO(s))

    This file also contain a sample strategy.
    For practice try import and use this file, by fixing TODO s
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
    # TODO: Try fill all the TODO to make the code work right
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
    print('Camera Image size:', TODO)   # Using OpenCV
    print('Camera Image dtype:', TODO)  # Using OpenCV


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
