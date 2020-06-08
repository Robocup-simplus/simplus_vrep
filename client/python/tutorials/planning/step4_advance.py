import client
from simplus_pb2 import *
import numpy as np
import cv2 as cv
import time
import enum


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

""" Here I used RCJRVision Library for detecting H,S, and U Letters
    For installation use: pip install RCJRVision
"""
from RCJRVision import RCJRVision

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
    turnless_backward = 4
    invalid = 5


def ang_normalize(ang):
    if ang > 180:
        return ang - 360
    if ang <= -180:
        return ang + 360
    return ang


# Move Class
class Move:
    def __init__(self):
        self.init_pos = np.zeros(4)
        self.is_move_started = False
        self.is_black_occurred = False

    def rotate(self, current_pos, direction):
        if direction == MoveType.forward:
            desired_ang = 0
        elif direction == MoveType.backward:
            desired_ang = 180
        elif direction == MoveType.left:
            desired_ang = 90
        else:
            desired_ang = -90

        error = ang_normalize(desired_ang - current_pos[3])
        if abs(error) < 0.5:
            return 0, 0, True
        else:
            return 0, error / 20, False

    def step_move(self, dist, color, current_pos, direction, vel):
        applied_vel = vel
        [lin, ang, is_done] = self.rotate(current_pos, direction)
        global last_vel

        if not self.is_move_started:
            self.init_pos = current_pos.copy()
            self.is_move_started = True
        if not is_done:
            last_vel = 0
            return lin, ang, False, False

        if color < 100 and not self.is_black_occurred:
            self.is_black_occurred = True

        if vel - last_vel > acc:
            applied_vel = last_vel + acc
        if dist[2].distance + dist[3].distance < 0.14:
            self.is_move_started = False
            last_vel = 0
            return 0, 0, True, False
        if self.is_black_occurred:
            if abs(current_pos[1] - self.init_pos[1]) > 0.01 or abs(
                    current_pos[0] - self.init_pos[0]) > 0.01:
                if dist[6].distance + dist[7].distance < 0.2:
                    self.is_move_started = False
                    last_vel = 0
                    return 0, 0, True, True
                return -0.05, 0, False, True
            else:
                self.is_move_started = False
                self.is_black_occurred = False
                last_vel = 0
                return 0, 0, True, True
        else:
            if abs(current_pos[1] - self.init_pos[1]) < 0.193333 and abs(
                    current_pos[0] - self.init_pos[0]) < 0.193333:
                last_vel = applied_vel
                return applied_vel, 0, False, False
            else:
                self.is_move_started = False
                last_vel = 0
                return 0, 0, True, False


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


def dir_rotate(direction, rotation):
    if str.lower(rotation) == 'l':
        if direction == MoveType.forward:
            dir = MoveType.left
        elif direction == MoveType.left:
            dir = MoveType.backward
        elif direction == MoveType.backward:
            dir = MoveType.right
        else:
            dir = MoveType.forward
    else:
        if direction == MoveType.forward:
            dir = MoveType.right
        elif direction == MoveType.left:
            dir = MoveType.forward
        elif direction == MoveType.backward:
            dir = MoveType.left
        else:
            dir = MoveType.backward
    return dir


def simple_evaluate(current_location, distances, is_front_tie_black):
    if not distances[0].distance and not distances[1].distance and not distances[2].distance \
            and not distances[3].distance and not distances[4].distance and not distances[5].distance \
            and not distances[6].distance and not distances[7].distance:
        return MoveType.invalid
    if distances[5].distance > 0.15 or not distances[5].detected:
        return ang_to_dir(current_location[3] - 90)
    elif not is_front_tie_black and distances[2].distance + distances[3].distance > 0.3 \
            or not distances[2].detected or not distances[3].detected:
        return ang_to_dir(current_location[3])
    elif distances[0].distance > 0.15 or not distances[0].detected:
        return ang_to_dir(current_location[3] + 90)
    else:
        return ang_to_dir(current_location[3] + 180)


# Convert raw image to open cv image
def convert_to_cv_img(img_raw, h, w):
    img_array = np.frombuffer(img_raw, dtype=np.uint8)
    img = img_array.reshape(h, w, 3)
    img_center = (w / 2, h / 2)
    mirrored_img = cv.getRotationMatrix2D(img_center, 180.0, 1.0)
    main_img = cv.warpAffine(img, mirrored_img, (w, h))
    main_img = cv.flip(main_img, 1)
    return main_img


# find victim
def find_victim(img, dist, pos, h_img=None):
    my_vision = RCJRVision.HSUVision()
    if dist[2] and dist[3] and dist[2].distance + dist[3].distance < 0.2 and \
            (abs(pos[3] - 90) < 3 or abs(pos[3] + 90) < 1
             or abs(pos[3]) < 3 or abs(pos[3] - 180) < 1
             or abs(pos[3] + 180) < 1):
        letter, center = my_vision.find_HSU(img)
        if letter:
            # cv.imwrite('{}--{}--{}.jpg'.format(letter, dist[2].distance + dist[3].distance, pos[3]), img)
            return letter
        else:
            return None


is_started = False
is_move_done = True
dir_to_go = MoveType.forward
start_point = np.zeros(4)
current_point = np.zeros(4)
is_step_done = False
is_check_done_L = False
is_check_done_R = False
robot_move = Move()
can_turn_l = False
can_turn_r = False
victims = []
last_vel = 0
acc = 0.025
is_victim_available = False
find_time = 0
state = 'Running'
is_front_tie_black = False
def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """

    # Get camera image and convert to an open cv image
    img = convert_to_cv_img(observation.camera.raw, observation.camera.h, observation.camera.w)

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
    global is_step_done
    global is_check_done_L
    global is_check_done_R
    global can_turn_l
    global can_turn_r
    global victims
    global is_victim_available
    global find_time
    global state
    global is_front_tie_black
    floor_light = observation.colors[0].r + observation.colors[0].g + observation.colors[0].b

    if state != 'End':
        victim = find_victim(img, observation.distances, local_pos)
        if victim:
            victims.append(victim)
            victims = list(dict.fromkeys(victims))
    if is_move_done:

        if is_victim_available:
            time.sleep(4)
            command.LED = 'dsad'
            is_victim_available = False
        dir_to_go = simple_evaluate(local_pos, observation.distances, is_front_tie_black)
        if dir_to_go != MoveType.invalid:
            is_move_done = False

    else:
        if not is_step_done:
            [command.linear, command.angular, is_step_done, is_front_tie_black] = robot_move.step_move(observation.distances, floor_light,
                                                                                   local_pos, dir_to_go, 0.2)
            can_turn_l = observation.distances[0].distance < 0.2 and observation.distances[0].detected
            can_turn_r = observation.distances[5].distance < 0.2 and observation.distances[5].detected

        else:
            # print('step')
            state = 'Start'
            if is_front_tie_black:
                is_move_done = True
                is_step_done = False
                is_check_done_L = False
                is_check_done_R = False
                victims.clear()
                return
            if not is_check_done_L and can_turn_l:
                # print('rotate L')
                [command.linear, command.angular, is_check_done_L] = \
                    robot_move.rotate(local_pos, dir_rotate(dir_to_go, 'l'))
            else:
                is_check_done_L = True

                if not is_check_done_R and can_turn_r:
                    # print('rotate R')
                    [command.linear, command.angular, is_check_done_R] = \
                        robot_move.rotate(local_pos, dir_rotate(dir_to_go, 'r'))
                else:
                    is_check_done_R = True
                    [command.linear, command.angular, is_back_done] = \
                        robot_move.rotate(local_pos, dir_to_go)
                    if is_back_done:
                        state = 'End'
                        # print('done')
                        for v in victims:
                            print(v)
                            command.actions.append(Action(x=observation.pos.x, y=observation.pos.y, z=observation.pos.z,
                                                              type='find_Victim'.format(v)))
                            command.actions.append(Action(x=observation.pos.x, y=observation.pos.y, z=observation.pos.z,
                                                              type='find_Victim_{0}'.format(v)))
                            if v == 'H':
                                command.LED = 'red'
                            if v == 'U':
                                command.LED = 'green'
                            if v == 'S':
                                command.LED = 'blue'
                            is_victim_available = True

                        is_move_done = True
                        is_step_done = False
                        is_check_done_L = False
                        is_check_done_R = False
                        victims.clear()


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