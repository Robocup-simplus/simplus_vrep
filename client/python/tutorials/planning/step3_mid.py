import client
from simplus_pb2 import *
import numpy as np
import time
import cv2 



    
info = WorldInfo()  # You can access world info everywhere


def control(observation):
        # Working with proximity sensor

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

        sensivity = 10  # Higher number means robot more afraid of hitting obstacles
        detected_obstacle = []
        for i, sensor in enumerate(observation.distances):
            if sensor.detected == True and sensor.distance < 1 / sensivity:
                detected_obstacle.append(i)  # There is an obstacle near sensor number "i"

        left_1 = 0
        left_2 = 1
        front_1 = 2
        front_2 = 3
        right_1 = 4
        right_2 = 5
        back_right = 6
        back_left = 7

        global PRE_MOVE
        direction=''


        ########## hole detection
        is_black_center = False
        is_black_left = False    
        is_black_right = False
        sum_center = (observation.colors[0].r + observation.colors[0].g + observation.colors[0].b) 
        if ( sum_center >5 and sum_center<30):
            is_black_center = True  

        sum_left= (observation.colors[1].r + observation.colors[1].g + observation.colors[1].b) 
        if ( sum_left >5 and sum_left<30):
            is_black_left = True  

        sum_right= (observation.colors[2].r + observation.colors[2].g + observation.colors[2].b) 
        if ( sum_right >5 and sum_right<30):
            is_black_right = True  

        ########### decide #########

        if front_1 not in detected_obstacle and front_2 not in detected_obstacle and not is_black_center:  # FORWARD
            return 'FORWARD'
        elif (left_1 not in detected_obstacle or left_2 not in detected_obstacle) and not  is_black_left:
            direction = 'TURN_LEFT'
        elif (right_1 not in detected_obstacle or right_2 not in detected_obstacle) and not is_black_right:
            direction = 'TURN_RIGHT'
        elif back_right not in detected_obstacle:
            direction = 'TURN_RIGHT'
        elif back_left not in detected_obstacle:
            direction = 'TURN_LEFT'
        else:
            direction = PRE_MOVE
        PRE_MOVE = direction

        return direction;


startTime= int(time.time() % 60)

def  is_robot_finished(observation,server):
     # TODO 
     #implement your own finish condition algorithm
    red_tile = False
    for c in observation.colors:
        if c.r > 190 and c.g<20 and c.b < 20: #red
            red_tile=True
    if not red_tile:
        return False
    global startTime
    now = int(time.time() % 60)  
    if now-startTime>60:   #after 60 seconds = 1 minute 
        return True
    return False


# Convert raw image to open cv image
def convert_to_cv_img(img_raw, h, w):
    img_array = np.frombuffer(img_raw, dtype=np.uint8)
    img = img_array.reshape(h, w, 3)
    img_center = (w / 2, h / 2)
    mirrored_img = cv2.getRotationMatrix2D(img_center, 180.0, 1.0)
    main_img = cv2.warpAffine(img, mirrored_img, (w, h))
    main_img = cv2.flip(main_img, 1)
    return main_img


def find_victim(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #bound the images
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    i=0
    victims=[]
    img_h,img_w = img.shape
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #improve the conditions
        if (img_w - w)<20 or (img_h - h)<20:
            continue
        if w<20 or h<20:
            continue
            #save individual images
        victims.append((x,y,h,w))
        i=i+1

    return victims


def is_victim_found(observation):

    img = convert_to_cv_img(observation.camera.raw, observation.camera.h, observation.camera.w)
    victims = find_victim(img)
    # TODO
    # double check the patches
    if len(victims)> 0:
      x,y,h,w = victims[0]
      print("find_victim",len(victims))
      return True
    return False



def is_checkpoint_found(observation):
    for c in observation.colors:
       if(c.r>100 and c.r<215 and c.g<215 and c.b<215 and abs(int(c.r)-int(c.g))<45 and abs(int(c.g)-int(c.b))<45 and  abs(int(c.r)-int(c.b))<45 ): #silver
          return True
    return False



def already_visited(observation):
    global victims_Visited
    for victim in  victims_Visited:
        x,y,z = victim
        tmp= pow(observation.pos.x - x, 2) + pow(observation.pos.y - y, 2) + pow(
                observation.pos.z - z, 2)
        distance= pow(tmp, 0.5)
        if distance < 0.25:
           return True;
    return False

def Start(world_info, team_info):
    """ THIS FUNCTION WILL BE CALLED IN THE BEGINING
        world_info : IN  {team_count, robot_per_team, color_sensors, distance_sensors, check_points}
        team_info  : OUT {name}
    """
    global info
    info = world_info
    # Fill your team information
    team_info.name = 'Dragon'


def End(server, result):
    """ THIS FUNCTION WILL BE CALLED AT THE END
        server : IN server Infomation {time, score, state}
        result : OUT {message, map}
    """
    # Get ending server info from server

    # Fill your final result here

    result.message = 'Good game!'




PRE_MOVE = 'STOP'  # Store previous turn in this variable
victims_Visited=[]

def Play(id, server, observation, command):
    """ THIS FUNCTION WILL BE CALLED FOR EACH ROBOT
        id         : IN robot ID
        server     : IN server Infomation {time, score, state}
        observation: IN {camera, position, color[], distance[]}
        command    : OUT {linear, angular, LED, actions[]}
    """

   # send action
    global victims_Visited


    if  is_robot_finished(observation,server):
       command.actions.append(Action(x=observation.pos.x,y=observation.pos.y,z=observation.pos.z,type='exit')) # type -> exit

    if not already_visited(observation) and is_victim_found(observation) :
       victims_Visited.append((observation.pos.x,observation.pos.y,observation.pos.z))
       # for recieving the victim score
       command.actions.append(Action(x=observation.pos.x,y=observation.pos.y,z=observation.pos.z,type='find_victim')) 
       # for recieving type identification score
       # find_victim_U, find_victim_H, find_victim_S, find_victim_Heated
       command.actions.append(Action(x=observation.pos.x,y=observation.pos.y,z=observation.pos.z,type='find_victim_U'))

    if is_checkpoint_found(observation) : # only for practice 
        command.actions.append(Action(x=observation.pos.x,y=observation.pos.y,z=observation.pos.z,type='find_checkpoint')) 

    

    # move
    direction = control(observation) 

    if direction == 'FORWARD':
        command.linear =  0.1
        command.angular = 0.0
    if direction == 'BACKWARD':
        command.linear = -0.1 
        command.angular = 0.0
    if direction == 'TURN_LEFT':
        command.linear = 0.0
        command.angular = 0.3
    if direction == 'TURN_RIGHT':
        command.linear = 0.0 
        command.angular = -0.3  
    if direction == 'STOP':
        command.linear = 0.0
        command.angular = 0.0
