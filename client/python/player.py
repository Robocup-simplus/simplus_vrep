import client
from simplus_pb2 import *
import numpy as np
import cv2 as cv
import time
import enum

info = WorldInfo()  # You can access world info everywhere

startPoint = [0, 0]


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


test_time = time.time_ns()
start_time = time.time()


# Type of each cell
class CellType(enum.Enum):
    blank = 0
    black = 1
    checkPoint = 2
    unDefined = 3


# Cells of the map class
class Cell:
    """ surrounding  
        True = wall
        False = No Wall
        0 -> Left
        1 -> Forward
        2 -> Right
        3 -> Back
    """
    victims = []
    type = CellType.unDefined

    def __init__(self, pos, surrounding):
        self.pos = pos
        is_visited = True
        self.surrounding = surrounding

    def add_victim(self, victim):
        self.victims.append(victim)

    def set_type(self, cell_type):
        self.type = cell_type


# Map class
class Map:
    map: [Cell] = []

    def add_new_cell(self, pos, surrounding):
        temp_cell = Cell(pos, surrounding)
        self.map.append(temp_cell)


# Type of steps
class MoveType(enum.Enum):
    forward = 0
    backward = 1
    right = 2
    left = 3
    turn_backward = 4
    invalid = 5


def ang_normalize(ang):
    if ang > 180:
        return ang - 360
    if ang < -180:
        return ang + 360
    return ang


# Move Class
class Move:
    def __init__(self):
        self.init_pos = np.zeros(4)
        self.is_move_started = False

    def rotate(self, current_pos, direction):
        if direction == MoveType.forward:
            desired_ang = 0
        elif direction == MoveType.backward:
            desired_ang = 180
        elif direction == MoveType.left:
            desired_ang = 90
        else:
            desired_ang = -90

        if ang_normalize(desired_ang - current_pos[3]) > 0.5:
            return 0, min(abs(desired_ang - current_pos[3]) / 20, 0.95) + 0.1, False
        if ang_normalize(desired_ang - current_pos[3]) < -0.5:
            return 0, -1 * min(abs(desired_ang - current_pos[3]) / 20, 0.95) - 0.1, False
        else:
            return 0, 0, True

    def step_move(self, dist, current_pos, direction, vel):
        [lin, ang, is_done] = self.rotate(current_pos, direction)
        if not self.is_move_started:
            self.init_pos = current_pos.copy()
            self.is_move_started = True
        if not is_done:
            return lin, ang, False
        if dist[2].distance + dist[3].distance < 0.14:
            self.is_move_started = False
            return 0, 0, True
        if abs(current_pos[1] - self.init_pos[1]) < 0.1933333333 and abs(current_pos[0] - self.init_pos[0]) < 0.1933333333:
            return vel, 0, False
        else:
            self.is_move_started = False
            return 0, 0, True



def ang_to_dir(ang_in):
    ang = ang_normalize(ang_in)
    if abs(ang) < 10:
        return MoveType.forward
    elif abs(ang - 90) < 10:
        return MoveType.left
    elif abs(ang + 90) < 10:
        return MoveType.right
    else:
        return MoveType.backward


def simple_evaluate(current_location, distances):
    if not distances[0].distance and not distances[1].distance and not distances[2].distance\
            and not distances[3].distance and not distances[4].distance and not distances[5].distance\
            and not distances[6].distance and not distances[7].distance:
        return MoveType.invalid
    if distances[5].distance > 0.15 or not distances[5].detected:
        return ang_to_dir(current_location[3] - 90)
    elif distances[2].distance + distances[3].distance > 0.3 \
            or not distances[2].detected or not distances[3].detected:
        return ang_to_dir(current_location[3])
    elif distances[0].distance > 0.15 or not distances[0].detected:
        return ang_to_dir(current_location[3] + 90)
    else:
        return ang_to_dir(current_location[3] + 180)


is_started = False
is_move_done = True
dir_to_go = MoveType.forward
start_point = np.zeros(4)
current_point = np.zeros(4)

robot_move = Move()


def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """
    global test_time
    dif_time = time.time() - start_time
    # print("dif time =", 1000000000 / (time.time_ns() - test_time))
    # test_time = time.time_ns()

    global is_started
    global start_point
    global current_point
    if not is_started:
        start_point[0] = observation.pos.x
        start_point[1] = observation.pos.y
        start_point[2] = observation.pos.z
        start_point[3] = observation.pos.yaw
        is_started = True
    global_pos = np.zeros(4)
    global_pos[0] = observation.pos.x
    global_pos[1] = observation.pos.y
    global_pos[2] = observation.pos.z
    global_pos[3] = observation.pos.yaw

    local_pos = global_pos - start_point

    global robot_move
    global is_move_done
    global dir_to_go
    if is_move_done:
        dir_to_go = simple_evaluate(local_pos, observation.distances)
        print(observation.distances)
        print(dir_to_go)
        if dir_to_go != MoveType.invalid:
            is_move_done = False
        # time.sleep(0.5)
    else:
        [command.linear, command.angular, is_done] = robot_move.step_move(observation.distances, local_pos, dir_to_go,
                                                                          0.15)
        # [command.linear, command.angular, is_done] = robot_move.rotate(local_pos,dir_to_go)
        if is_done:
            is_move_done = True
    # print(observation.distances)

    # col = ['red', 'green', 'blue', 'akldjf']
    # a = [0, 0, 0]
    # for c in observation.colors:
    #     a[0] += c.r
    #     a[1] += c.g
    #     a[2] += c.b
    # command.LED = col[int(np.argmax(a))]
    # obstacle = 0
    # for i in range(1, 5):
    #     obstacle += observation.distances[i].detected
    #
    # # if obstacle == 0:
    # #     command.linear = 0.00
    # #     command.angular = 0.0
    # # else:
    # #     command.linear = 0.0
    # #     command.angular = 0.0
    #
    # for c in observation.colors:
    #    if(c.r>100 and c.r<215 and c.g<215 and c.b<215 and abs(int(c.r)-int(c.g))<45 and abs(int(c.g)-int(c.b))<45 and  abs(int(c.r)-int(c.b))<45 ):
    #        command.actions.append(Action(x=observation.pos.x,y=observation.pos.y,z=observation.pos.z,type='find_checkpoint'))
    #        break
    #
    # img_raw = observation.thermalCamera.raw
    # img_array = np.frombuffer(img_raw, dtype=np.uint8)
    # img = img_array.reshape(observation.thermalCamera.h,observation.thermalCamera.w,3)
    # img_center = (observation.thermalCamera.w / 2, observation.thermalCamera.h / 2)
    # M = cv.getRotationMatrix2D(img_center, 180.0, 1.0)
    # main_img = cv.warpAffine(img, M, (observation.thermalCamera.w, observation.thermalCamera.h))
    # main_img = cv.flip(main_img,1)
    # cv.imwrite('a.jpg',main_img)
