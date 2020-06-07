"""
This is the sample class for more advanced version of player API

It's recommended to normal api `sample.py` if you are not familiar with OOP in python
This version brings to advantage in favor of performance or accuracy it's just clean-code API
"""
from client.python.base_player import BasePlayer


class SamplePlayer(BasePlayer):
    def __init__(self):
        super().__init__()

    def Start(self, world_info, team_info):
        """ THIS FUNCTION WILL BE CALLED IN THE BEGINING
            world_info : IN  {team_count, robot_per_team, color_sensors, distance_sensors, check_points}
            team_info  : OUT {name}
        """
        self.info = world_info
        team_info.name = 'my_team_name'

    def End(self, server, result):
        """ THIS FUNCTION WILL BE CALLED AT THE END
            server : IN server Infomation {time, score, state}
            result : OUT {message, map}
        """
        result.message = 'The Ending Message'

    def Play(self, id, server, observation, command):
        """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
            id         : IN robot ID
            server     : IN server Infomation {time, score, state}
            observation: IN {camera, position, color[], distance[], heatCamera}
            command    : OUT {linear, angular, LED, victims[]}
        """
        obstacle = 0
        for i in range(8):
            obstacle += observation.distances[0].distance
            print(observation.distances[0].detected, observation.distances[0].distance)

        if (obstacle == 0):
            command.linear = 0.01
            command.angular = 0.0
        else:
            command.linear = 0.0
            command.angular = 0.1