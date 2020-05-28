"""
This is the base class for more advanced version of player API

It's recommended to normal api `sample.py` if you are not familiar with OOP in python
This version brings to advantage in favor of performance or accuracy it's just clean-code API
"""
import client
from simplus_pb2 import *

""" You should inherite this class and create a new player (See. advance_sample.py)"""


class BasePlayer:
    def __init__(self):
        self.info = WorldInfo()  # You can access world info everywhere

    def Start(self, world_info, team_info):
        """ THIS FUNCTION WILL BE CALLED IN THE BEGINING
            world_info : IN  {team_count, robot_per_team, color_sensors, distance_sensors, check_points}
            team_info  : OUT {name}
        """
        pass

    def End(self, server, result):
        """ THIS FUNCTION WILL BE CALLED AT THE END
            server : IN server Infomation {time, score, state}
            result : OUT {message, map}
        """
        pass

    def Play(self, id, server, observation, command):
        """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
            id         : IN robot ID
            server     : IN server Infomation {time, score, state}
            observation: IN {camera, position, color[], distance[], heatCamera}
            command    : OUT {linear, angular, LED, victims[]}
        """
        pass
