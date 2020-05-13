try:
    import vrep
except:
    print('--------------------------------------------------------------')
    print('"vrep.py" could not be imported. This means very probably that')
    print('either "vrep.py" or the remoteApi library could not be found.')
    print('Make sure both are in the same folder as this file,')
    print('or appropriately adjust the file "vrep.py"')
    print('--------------------------------------------------------------')
    print('')

import time
import numpy as np
# from matplotlib import pyplot as plt
import math

#scratch
import simplus_scratch
#endscratch

class VrepApi:
    def __init__(self, server_ip='127.0.0.1', server_port=19999, waitUntilConnected=True,
                 doNotReconnectOnceDisconnected=True, timeOutInMs=5000, commThreadCycleInMs=5):
        vrep.simxFinish(-1)  # just in case, close all opened connections
        self.clientID = vrep.simxStart(server_ip, server_port, waitUntilConnected, doNotReconnectOnceDisconnected,
                                       timeOutInMs, commThreadCycleInMs)  # Connect to V-REP
        print("client id", self.clientID)
        self.robot_api = None
        self.server_api = None

    def init_robotApi(self, trapConfig=r'trapconfig.txt', robot_base='ePuck_base', robot_namespace="ePuck_",
                      robot_motors={"left": 'leftJoint', "right": 'rightJoint', "radius": 0.02},
                      proximity_sensor={"num": 8, "name": 'proxSensor'}, camera={"name": 'camera', "joint": None},
                      color_sensor={"num": 1, "name": 'lightSensor'}, gps_enabled=True,
                      thermal_camera={"name": 'thermalCamera', "joint":None},penaltyStopTime=10,checkPointConfig=r'checkpointconfig.txt'):
        return robotApi(remoteApi=self.clientID, trapConfig=trapConfig, robot_base=robot_base,
                        robot_namespace=robot_namespace, robot_motors=robot_motors, proximity_sensor=proximity_sensor,
                        camera=camera, color_sensor=color_sensor, gps_enabled=gps_enabled,
                        thermal_camera=thermal_camera,penaltyStopTime=penaltyStopTime)

    def init_serverApi(self,
                       actionConfig=r'actionconfig.txt',checkPointConfig=r'checkpointconfig.txt',victimConfig=r'victimconfig.txt'):
        return serverApi(remoteApi=self.clientID, actionConfig=actionConfig,checkPointConfig=checkPointConfig,victimConfig=victimConfig)


class actionClass:
    def __init__(self, remoteApi, action, max_range=1.0, success_score=1.0, failure_score=-0.5, obejcts_names=[],multiplier_coefficient=0):
        self.action = action
        self.clientID = remoteApi
        self.range = float(max_range)
        self.success_score = float(success_score)
        self.failure_score = float(failure_score)
        self.obejcts_names = obejcts_names
        self.objects_distances = []
        self.multiplier_coefficient=multiplier_coefficient;
        self.seen_list=[]
        for i in self.obejcts_names:
            temp1, oh = vrep.simxGetObjectHandle(self.clientID, i, vrep.simx_opmode_blocking)
            response = vrep.simxGetObjectPosition(self.clientID, oh, -1, vrep.simx_opmode_blocking)
            self.objects_distances.append([response[1][0], response[1][1], response[1][2]])

    def applyAction(self, x, y, z,current_score=0):
        target_distances = []
#         print("Seen=",self.seen_list)
        for i in range(0, len(self.objects_distances)):
            s = pow(self.objects_distances[i][0] - x, 2) + pow(self.objects_distances[i][1] - y, 2) + pow(
                self.objects_distances[i][2] - z, 2)
            target_distances.append(pow(s, 0.5))
        index_min = np.argmin(np.array(target_distances))
        if target_distances[index_min] <= self.range and not(index_min in self.seen_list):
            self.logAction(x, y, z, index_min, target_distances[index_min], self.success_score)
            self.seen_list.append(index_min)
            action_score=self.success_score
            if(current_score>0):
                action_score+= current_score*(self.multiplier_coefficient-1)
            return action_score
        else:
            self.logAction(x, y, z, index_min, target_distances[index_min], self.failure_score)
            return self.failure_score,None

    def logAction(self, x, y, z, index_min, distance, score):
         if score==0:
            print("ACTION: ",self.action," Was requested on point : ",x, y, z,"---- Distance from center of action: ",distance,"---- Recieved score:",score," --- It's Duplicated action!!")     
         else:
            print("ACTION: ",self.action," Was requested on point : ",x, y, z,"---- Distance from center of action: ",distance,"---- Recieved score:",score)
#         print(self.action)
#         print(x, y, z)
#         print(self.obejcts_names[index_min], self.objects_distances[index_min])
#         print(distance, score)


class trapClass:
    def __init__(self, remoteApi, trap, trap_size=1.0, penalty=1.0, bandgap_range=0.5, obejcts_names=[]):
        self.trap_activated = False
        self.trap = trap
        self.clientID = remoteApi
        self.trap_size = float(trap_size)
        self.penalty = float(penalty)
        self.bandgap_range = float(bandgap_range)
        self.obejcts_names = obejcts_names
        self.objects_distances = []
        for i in self.obejcts_names:
            temp1, oh = vrep.simxGetObjectHandle(self.clientID, i, vrep.simx_opmode_blocking)
            response = vrep.simxGetObjectPosition(self.clientID, oh, -1, vrep.simx_opmode_blocking)
            self.objects_distances.append([response[1][0], response[1][1], response[1][2]])

    def checkInsideTrap(self,trapPoses,robotPoses):
        for i in [0,1]:
            if(robotPoses[i]>(trapPoses[i]+self.trap_size/2)) or (robotPoses[i]<(trapPoses[i]-self.trap_size/2)):
                return False;
        return True;

    def checkTrap(self, x, y, z):
        target_distances = []
        # first we find the closest trap
        for i in range(0, len(self.objects_distances)):
            s = pow(self.objects_distances[i][0] - x, 2) + pow(self.objects_distances[i][1] - y, 2) + pow(
                self.objects_distances[i][2] - z, 2)
            target_distances.append(pow(s, 0.5))
        index_min = np.argmin(np.array(target_distances))
        # now we check if the robot is in the closest trap
        if self.checkInsideTrap(self.objects_distances[index_min],[x,y,z]):
            self.logTrap(x, y, z, index_min, target_distances[index_min])
            return self.penalty
        else:
            return 0

    def logTrap(self, x, y, z, index_min, distance):
          print("TRAP: ",self.trap," Passed point : ",x, y, z,"---- Distance from center of trap: ",distance,"---- Recieved score: ",self.penalty)

#         print(self.trap)
#         print(x, y, z)
#         print(self.obejcts_names[index_min], self.objects_distances[index_min])
#         print(distance)



class CheckPointClass:
    def __init__(self, remoteApi, checkPoint, checkPoint_size=1.0, success_score=1.0, failure_score=0.0, obejcts_names=[]):
        self.checkPoint = checkPoint
        self.clientID = remoteApi
        self.checkPoint_size = float(checkPoint_size)
        self.success_score = float(success_score)
        self.failure_score = float(failure_score)
        self.obejcts_names = obejcts_names
        self.objects_distances = []
        self.seen_checkpoints=[]
        for i in self.obejcts_names:
            temp1, oh = vrep.simxGetObjectHandle(self.clientID, i, vrep.simx_opmode_blocking)
            response = vrep.simxGetObjectPosition(self.clientID, oh, -1, vrep.simx_opmode_blocking)
            self.objects_distances.append([response[1][0], response[1][1], response[1][2]]);
            print("robot api , checkpoint name =>",i," x =>",response[1][0]," ###### y =>",response[1][1]," ##  z =>",response[1][2])
            self.seen_checkpoints.append(0)

    def checkInsideCheckPoint(self,checkPointPoses,robotPoses):
        for i in [0,1]:
            if(robotPoses[i]>(checkPointPoses[i]+self.checkPoint_size/2)) or (robotPoses[i]<(checkPointPoses[i]-self.checkPoint_size/2)):
                return False;
        return True;

    def checkAllCheckPoints(self, x, y, z):
        target_distances = []
        # first we find the closest checkpoint
        for i in range(0, len(self.objects_distances)):
            s = pow(self.objects_distances[i][0] - x, 2) + pow(self.objects_distances[i][1] - y, 2) + pow(
                self.objects_distances[i][2] - z, 2)
            target_distances.append(pow(s, 0.5))
        index_min = np.argmin(np.array(target_distances))
        # now we check if the robot is in the closest checkpoint
        if not self.checkInsideCheckPoint(self.objects_distances[index_min],[x,y,z]):
            self.logCheckPoint(x, y, z, index_min, target_distances[index_min],self.failure_score)
            return self.failure_score,None;
            
        elif self.seen_checkpoints[index_min]==0:
            self.seen_checkpoints[index_min]=1;
            self.logCheckPoint(x, y, z, index_min, target_distances[index_min],self.success_score)
            return self.success_score,self.objects_distances[index_min];
        else:
            self.logCheckPoint(x, y, z, index_min, target_distances[index_min],0)
            return 0,self.objects_distances[index_min];

    def logCheckPoint(self, x, y, z, index_min, distance,score=0):
          print("checkpoint: ",self.checkPoint," Passed point : ",x, y, z,"---- Distance from center of checkpoint: ",distance,"---- Recieved score: ",score)

#         print(self.trap)
#         print(x, y, z)
#         print(self.obejcts_names[index_min], self.objects_distances[index_min])
#         print(distance)


class robotApi:

    def __init__(self, remoteApi, trapConfig=None, robot_base='ePuck', robot_namespace="ePuck_",
                 robot_motors={"left": 'leftJoint', "right": 'rightJoint', "radius": 0.02},
                 proximity_sensor={"num": 8, "name": 'proxSensor'}, camera={"name": 'camera', "joint": None},
                 color_sensor={"num": 1, "name": 'lightSensor'}, gps_enabled=True,
                 thermal_camera={"name": 'thermalCamera', "joint": None},penaltyStopTime=5,checkPointConfig=None):
        self.gps_enabled = gps_enabled
        self.clientID = remoteApi
        temp1, self.left = vrep.simxGetObjectHandle(self.clientID, robot_namespace + robot_motors["left"],
                                                    vrep.simx_opmode_blocking)
        temp2, self.right = vrep.simxGetObjectHandle(self.clientID, robot_namespace + robot_motors["right"],
                                                     vrep.simx_opmode_blocking)
        self.wheel_radius = robot_motors["radius"]
        temp3, self.robot_base = vrep.simxGetObjectHandle(self.clientID, robot_base, vrep.simx_opmode_blocking)
        self.robot_width = self.__getRobotWidth__()
        temp4, self.camera = vrep.simxGetObjectHandle(self.clientID, robot_namespace + camera["name"],
                                                      vrep.simx_opmode_blocking)
        temp5, self.thermal_camera = vrep.simxGetObjectHandle(self.clientID, robot_namespace + thermal_camera["name"],
                                                              vrep.simx_opmode_blocking)
        if camera["joint"]:
            temp, self.camera_joint = vrep.simxGetObjectHandle(self.clientID, robot_namespace + camera["joint"],
                                                               vrep.simx_opmode_blocking)
        else:
            self.camera_joint = None

        self.proxSensors = []
        for i in range(1, proximity_sensor["num"] + 1):
            temp, sensor = vrep.simxGetObjectHandle(self.clientID, robot_namespace + proximity_sensor["name"] + str(i),
                                                    vrep.simx_opmode_blocking)
            self.proxSensors.append(sensor)

        self.colorSensors = []
        for i in ['', '_l', '_r']:
            temp, sensor = vrep.simxGetObjectHandle(self.clientID, robot_namespace + color_sensor["name"] + str(i),
                                                    vrep.simx_opmode_blocking)
            self.colorSensors.append(sensor)

        self.traps_dict = None
        if (trapConfig != None):
            self.traps_dict = {}
            self.parseConfig(trapConfig)

        self.checkPoint_dict=None
        if (checkPointConfig != None):
            self.checkPoint_dict = {}
            self.parseCheckPointConfig(checkPointConfig)
        
        self.checkPointTilePose=self.getRobotXYZ()
        if(self.checkPointTilePose[0]==0 and self.checkPointTilePose[1]==0  ):
            self.checkPointTilePose=[10,10]
        self.penaltyStopTime=penaltyStopTime;
        self.frozen=False;
        self.freezTime=0;

    def setCheckPointTile(self,pose):
        if(pose==None):
            print("robotapi shit getting null pose for checkpoint")
            return 
        print("robotapi setting checkpoint")
        self.checkPointTilePose=pose
        return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_set_checkpoint',
                                                                                      [], [pose[0],pose[1]], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_oneshot)

    def freezRobot(self):
        print("robotapi freezing robot")
        self.frozen=True;
        self.setRobotSpeed(0,0);
        x,y=self.checkPointTilePose[0],self.checkPointTilePose[1]
        return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_set_robot_pose',
                                                                                      [], [x,y], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_oneshot)

    def checkFrozenRobot(self):
        print("robotapi freeze time ",self.freezTime )
        print("robotapi freeze time ",self.penaltyStopTime )

        if(self.freezTime>self.penaltyStopTime):
            print("robot api heating the robot ")
            self.frozen=False;
            self.freezTime=0;
        else:
            self.freezTime+=1

    def precompute(self):
        vrep.simxGetObjectPosition(self.clientID, self.right, self.robot_base,vrep.simx_opmode_streaming)
        vrep.simxGetObjectPosition(self.clientID, self.left, self.robot_base, vrep.simx_opmode_streaming) 
        vrep.simxGetObjectPosition(self.clientID, self.robot_base, -1,vrep.simx_opmode_streaming)    
        vrep.simxGetObjectOrientation(self.clientID, self.robot_base, -1,vrep.simx_opmode_streaming)  
        vrep.simxGetVisionSensorImage(self.clientID, self.camera, 0,vrep.simx_opmode_streaming)
        vrep.simxGetVisionSensorImage(self.clientID,self.colorSensors[0], 0,vrep.simx_opmode_streaming)
        vrep.simxGetVisionSensorImage(self.clientID,self.colorSensors[1], 0,vrep.simx_opmode_streaming)
        vrep.simxGetVisionSensorImage(self.clientID,self.colorSensors[2], 0,vrep.simx_opmode_streaming)
        vrep.simxGetVisionSensorImage(self.clientID, self.thermal_camera, 0,vrep.simx_opmode_streaming)
        
    def __getRobotWidth__(self):
        response_right = vrep.simxGetObjectPosition(self.clientID, self.right, self.robot_base,
                                                    vrep.simx_opmode_blocking)
        response_left = vrep.simxGetObjectPosition(self.clientID, self.left, self.robot_base, vrep.simx_opmode_blocking)
        right_x, right_y = response_right[1][0:2]
        left_x, left_y = response_left[1][0:2]
        x_width = abs((left_x) - (right_x))
        y_width = abs((left_y) - (right_y))
        return max(x_width, y_width)

    def getRobotXYZ(self):
        position = vrep.simxGetObjectPosition(self.clientID, self.robot_base, -1,vrep.simx_opmode_blocking)
        return position[1]

    def checkAllTraps(self):
        penalty = 0
        pose = self.getRobotXYZ()

        for t in self.traps_dict.keys():
            penalty += self.traps_dict.get(t).checkTrap(pose[0],pose[1],pose[2])
        
        if not (penalty==0):
            self.freezRobot();
        if(self.frozen==True):
            self.checkFrozenRobot()
        return penalty

    def setLED(self, color):

        if (color == "red"):
            returnCode, outInts, outFloats, outStrings, outBuffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                                'Simplus_monitor',
                                                                                                vrep.sim_scripttype_childscript,
                                                                                                'remote_led_change',
                                                                                                [21002], [], [],
                                                                                                bytearray(),
                                                                                                vrep.simx_opmode_oneshot)
            if (returnCode == 0):
                return 'red'
            else:
                return -1
        if (color == "green"):
            returnCode, outInts, outFloats, outStrings, outBuffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                                'Simplus_monitor',
                                                                                                vrep.sim_scripttype_childscript,
                                                                                                'remote_led_change',
                                                                                                [21003], [], [],
                                                                                                bytearray(),
                                                                                                vrep.simx_opmode_oneshot)
            if (returnCode == 0):
                return 'green'
            else:
                return -1
        if (color == "blue"):
            returnCode, outInts, outFloats, outStrings, outBuffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                                'Simplus_monitor',
                                                                                                vrep.sim_scripttype_childscript,
                                                                                                'remote_led_change',
                                                                                                [21004], [], [],
                                                                                                bytearray(),
                                                                                                vrep.simx_opmode_oneshot)
            if (returnCode == 0):
                return 'blue'
            else:
                return -1
        else:
            returnCode, outInts, outFloats, outStrings, outBuffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                                'Simplus_monitor',
                                                                                                vrep.sim_scripttype_childscript,
                                                                                                'remote_led_change',
                                                                                                [21001], [], [],
                                                                                                bytearray(),
                                                                                                vrep.simx_opmode_oneshot)
            if (returnCode == 0):
                return ''
            else:
                return -1

    def getCameraImage(self):
        returnCode, image_resolution, image_array = vrep.simxGetVisionSensorImage(self.clientID, self.camera, 0,
                                                                                  vrep.simx_opmode_buffer)
        if (returnCode == 0 or returnCode == 1  ):
            return [image_array, image_resolution[0], image_resolution[1]]
        else:
            return -1
    def get_thermal_camera_image(self):
        return_code, image_resolution, image_array = vrep.simxGetVisionSensorImage(self.clientID,
                                                                                   self.thermal_camera, 0,
                                                                                   vrep.simx_opmode_buffer)
        if return_code == 0 or return_code == 1:
            return [image_array, image_resolution[0], image_resolution[1]]
        else:
            return -1

    def getColorSensor(self, sensor_index=0):
        if (sensor_index >= len(self.colorSensors)): return -1
        returnCode, image_resolution, image_array = vrep.simxGetVisionSensorImage(self.clientID,
                                                                                  self.colorSensors[sensor_index], 0,
                                                                                  vrep.simx_opmode_buffer)
        if (returnCode == 0 or returnCode == 1  ):
            image_array = (np.array(image_array, dtype=np.uint8))
            return image_array[24:27]
        else:
            print( returnCode, image_resolution, image_array)
            return -1

    def getProximitySensor(self, sensor_index=0):

        returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = vrep.simxReadProximitySensor(
            self.clientID, self.proxSensors[sensor_index], vrep.simx_opmode_oneshot)
        if (returnCode == 0 or returnCode == 1):
            if (detectionState == True):
                return [True, pow(pow(detectedPoint[0], 2) + pow(detectedPoint[1], 2) + pow(detectedPoint[2], 2), 0.5)]
            else:
                return [False, 0]
        else:
            print(returnCode,detectionState,detectedPoint )
            return -1

    def getRobotPose(self):
        returnCode_pose, position = vrep.simxGetObjectPosition(self.clientID, self.robot_base, -1,
                                                               vrep.simx_opmode_buffer)
        returnCode_orient, eulerAngles = vrep.simxGetObjectOrientation(self.clientID, self.robot_base, -1,
                                                                       vrep.simx_opmode_buffer)

        if ( (returnCode_pose == 0 or returnCode_pose == 1) and  (returnCode_orient == 0 or returnCode_orient == 1)):
            angles_in_degree = [(i + math.pi / 2) * 180 / math.pi for i in eulerAngles]

            if (self.gps_enabled):
                return [position[0], position[1], position[2], angles_in_degree[0], angles_in_degree[1],
                        angles_in_degree[2]]
            else:
                return [0, 0, 0, angles_in_degree[0], angles_in_degree[1], angles_in_degree[2]]

    def setRobotSpeed(self, linear=0.0, angular=0.0):
        if(self.frozen==True):return
        right_rotation = (linear + angular * self.robot_width / 2) / self.wheel_radius
        left_rotation = (linear - angular * self.robot_width / 2) / self.wheel_radius
        vrep.simxPauseCommunication(self.clientID, True)
        vrep.simxSetJointTargetVelocity(self.clientID, self.right, right_rotation, vrep.simx_opmode_oneshot)
        vrep.simxSetJointTargetVelocity(self.clientID, self.left, left_rotation, vrep.simx_opmode_oneshot)
        vrep.simxPauseCommunication(self.clientID, False)
        
    def setJointSpeed(self,right_rotation,left_rotation):
        if(self.frozen==True):return
        vrep.simxPauseCommunication(self.clientID,True)
        vrep.simxSetJointTargetVelocity(self.clientID,self.right,right_rotation,vrep.simx_opmode_oneshot)
        vrep.simxSetJointTargetVelocity(self.clientID,self.left,left_rotation,vrep.simx_opmode_oneshot)
        vrep.simxPauseCommunication(self.clientID,False)


    def parseConfig(self, config_file):
        with open(config_file, 'r') as fp:
            for line in fp:
                if(line[0]=='#'):continue;
                ls = line.split(';')
                ob = ls[1].split(',')
                ix = ls[2].split(',')
                ob_indexed = []
                for i in range(0, len(ob)):
                    temp = [ob[i]]
                    if (int(ix[i]) > 1):
                        for j in range(0, int(ix[i]) - 1):
                            temp.append(ob[i] + str(j))
                    ob_indexed.extend(temp)
                tc = trapClass(remoteApi=self.clientID, trap=ls[0], trap_size=ls[3], bandgap_range=ls[4], penalty=ls[5],
                               obejcts_names=ob_indexed)
                self.traps_dict.update({ls[0]: tc})

    def parseCheckPointConfig(self, config_file):
        with open(config_file, 'r') as fp:
            for line in fp:
                if(line[0]=='#'):continue;

                ls = line.split(';')
                ob = ls[1].split(',')
                ix = ls[2].split(',')
                ob_indexed = []
                for i in range(0, len(ob)):
                    temp = [ob[i]]
                    if (int(ix[i]) > 1):
                        for j in range(0, int(ix[i]) - 1):
                            temp.append(ob[i] + str(j))
                    ob_indexed.extend(temp)
                ac = CheckPointClass(remoteApi=self.clientID, checkPoint=ls[0], checkPoint_size=float(ls[3]), success_score=float(ls[4]),
                                 failure_score=float(ls[5]), obejcts_names=ob_indexed)
                self.checkPoint_dict.update({ls[0]: ac})

    def findCheckpoint(self):
        robot_pose=self.getRobotXYZ()
        x=robot_pose[0]
        y=robot_pose[1]
        z=robot_pose[2];
        score=0
        for action in self.checkPoint_dict.keys():
            s,poses=self.checkPoint_dict.get(action).checkAllCheckPoints(x, y, z)
            score+=s
            if(poses!=None):
                self.setCheckPointTile(poses)
            print("robotapi finding checkpoints ### pose =>", poses)
        return score
        






class serverApi:

    def __init__(self, remoteApi, actionConfig=None,checkPointConfig=None,victimConfig=None):
        self.clientID = remoteApi
        self.victim_dict=None
        self.actions_dict = None
        self.checkPoint_dict=None
        if (actionConfig != None):
            self.actions_dict = {}
            self.parseActionConfig(actionConfig)
        if (victimConfig != None):
            self.victim_dict = {}
            self.parseVictimConfig(victimConfig)

    def parseActionConfig(self, config_file):
        with open(config_file, 'r') as fp:
            for line in fp:
                if(line[0]=='#'):continue;
                ls = line.split(';')
                ob = ls[1].split(',')
                ix = ls[2].split(',')
                ob_indexed = []
                for i in range(0, len(ob)):
                    temp = [ob[i]]
                    if (int(ix[i]) > 1):
                        for j in range(0, int(ix[i]) - 1):
                            temp.append(ob[i] + str(j))
                    ob_indexed.extend(temp)
                ac = actionClass(remoteApi=self.clientID, action=ls[0], max_range=float(ls[3]), success_score=float(ls[5]),
                                 failure_score=float(ls[6]), obejcts_names=ob_indexed,multiplier_coefficient=float(ls[4]))
                self.actions_dict.update({ls[0]: ac})


    
    def parseVictimConfig(self, config_file):
        with open(config_file, 'r') as fp:
            for line in fp:
                if(line[0]=='#'):continue;

                ls = line.split(';')
                ob = ls[1].split(',')
                ix = ls[2].split(',')
                ob_indexed = []
                for i in range(0, len(ob)):
                    temp = [ob[i]]
                    if (int(ix[i]) > 1):
                        for j in range(0, int(ix[i]) - 1):
                            temp.append(ob[i] + str(j))
                    ob_indexed.extend(temp)
                ac = actionClass(remoteApi=self.clientID, action=ls[0], max_range=float(ls[3]), success_score=float(ls[4]),
                                 failure_score=float(ls[5]), obejcts_names=ob_indexed)
                self.victim_dict.update({ls[0]: ac})
    
    def callAction(self,action,x,y,z,score=0):
        if (action in self.actions_dict.keys()):
            score=self.actions_dict.get(action).applyAction(x, y, z)
            return score
        else:  
            return 0
    def findVictim(self, action, x, y, z):
        if (action in self.victim_dict.keys()):
            score=self.victim_dict.get(action).applyAction(x, y, z)
            return score
        else:
            
            return 0

    def set_score(self, team_id, team_score,isOneshot=True):
        if isOneshot:
           return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_set_score',
                                                                                      [team_id], [], [team_score],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_oneshot)
        else:
            return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_set_score',
                                                                                      [team_id], [], [team_score],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)      
        return return_code

    def set_name(self, team_name):
        return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_get_name',
                                                                                      [], [], [team_name],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)
        if len(o_int) > 1:
            return o_int[0],o_int[1]
        elif len(o_int) == 1:
            return o_int[0],1000
        else:
            return None
        
    def get_status(self,start=0,isOneshot=False):
        if isOneshot:
           return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_get_sim_status',
                                                                                      [start], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_oneshot)
        else:
           return_code, o_int, o_float, o_string, o_buffer = vrep.simxCallScriptFunction(self.clientID,
                                                                                      'Game_manager',
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      'remote_get_sim_status',
                                                                                      [start], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)
        if len(o_int) >= 1:
            return o_int[0]
        else:
            return None

    def getServerTime(self):
        response = vrep.simxGetServerTimeInMs(vrep.simx_opmode_blocking)
        if (response[0]):
            return response[1]
        else:
            return -1

    def getServerState(self):
        response = vrep.simxGetSimulationState(vrep.simx_opmode_blocking)
        if (response[0]):
            if (response[1] == 0):
                return "stopped"
            elif (response[1] == 8):
                return "paused"
            else:
                return "running"
        else:
            return -1

    def stopSimulation(self):
        response = vrep.simxStopSimulation(self.clientID, operationMode=vrep.simx_opmode_blocking)
        if (response == 0):
            print(response)
        else:
            return -1

    def startSimulation(self):
        response = vrep.simxStartSimulation(self.clientID, operationMode=vrep.simx_opmode_blocking)
        if (response):
            print("starign simulation")

            print(response)
        else:
            print("starign failed")
            return -1

    def pauseSimulation(self):
        response = vrep.simxPauseSimulation(self.clientID, vrep.simx_opmode_blocking)
        if (response):
            print(response)
        else:
            return -1


def show_image(inputimage):
    image_array = (np.array(inputimage[0], dtype=np.uint8))
    im = np.flip(np.reshape(image_array, [inputimage[1], inputimage[2], 3]), 0)
    print(im)
    # plt.imshow(im)
    # plt.show()




def main():
    vapi = VrepApi()
    sa = vapi.init_serverApi()
    is_started = sa.get_status(1)
    # sa.startSimulation()
    print("step1")
    time.sleep(0.1)
    ra = vapi.init_robotApi()
#     #scratch
#     st=simplus_scratch.ScratchThread(vapi,ra,sa)
#     st.start()
    #endscratch
    time.sleep(0.1)
    print("start precompute")
    ra.precompute()
    print("end precompute")

    counter = 0
    col = ['red', 'green', 'blue', 'akldjf']
    obstacle = 0
    team_score = 0
    my_team_id = 0
    r,game_duration=sa.set_name('my_team_name')
    print("game_duration=",game_duration)
    if r is None:
        r=0
    my_team_id = max(r, my_team_id)
    testtime=time.time_ns()
    while True:
        is_started = sa.get_status(isOneshot=True)
        while not is_started:
           is_started = sa.get_status(isOneshot=True)

        obstacle = 0
        col0 = ra.getColorSensor(0)
        col1 = ra.getColorSensor(1)
        col2 = ra.getColorSensor(2)


        if((col0[0]>100 and col0[0]<215 and col0[1]<215 and col0[2]<215 and abs(int(col0[0])-int(col0[1]))<45 and abs(int(col0[1])-int(col0[2]))<45 and  abs(int(col0[0])-int(col0[2]))<45 ) or
           (col1[0]>100 and col1[0]<215 and col1[1]<215 and col1[2]<215 and abs(int(col1[0])-int(col1[1]))<45 and abs(int(col1[1])-int(col1[2]))<45 and  abs(int(col1[0])-int(col1[2]))<45 ) or
           (col2[0]>100 and col2[0]<215 and col2[1]<215 and col2[2]<215 and abs(int(col2[0])-int(col2[1]))<45 and abs(int(col2[1])-int(col2[2]))<45 and  abs(int(col2[0])-int(col2[2]))<45) ):
            pos = ra.getRobotXYZ()
            team_score += sa.callAction("find_checkpoint", pos[0],pos[1], pos[2])

        col_total = (np.array(col0) + np.array(col1) + np.array(col2))
        ra.setLED(col[np.argmax(col_total)])

        for i in range(2, 6):
            obstacle += ra.getProximitySensor(i)[0]

        if (obstacle == 0):
            ra.setRobotSpeed(0.05, 0.0)
        else:
            ra.setRobotSpeed(0.00, 0.5)
        team_score += ra.checkAllTraps()
        sa.set_score(my_team_id, str(team_score),False)
        print("dif time =",1000000000/(time.time_ns()-testtime))
        testtime=time.time_ns()
       # time.sleep(0.25)
        counter += 1
        if (counter > game_duration): break
    sa.stopSimulation()
    vrep.simxFinish(vapi.clientID)
    time.sleep(25)



# def main2():
#     vapi = VrepApi()
#     sa = vapi.init_serverApi()
#     is_started = sa.get_status(1)
#     # sa.startSimulation()
#     print("step1")
#     time.sleep(0.1)
#     ra = vapi.init_robotApi()
    

if __name__ == '__main__':
    main()