from __future__ import print_function
import logging

import grpc

import simplus_pb2
import simplus_pb2_grpc
from robotApi import *
import time
import array
import numpy as np
import simplus_scratch


port_number=4719
def run():

     vapi = VrepApi()
     sa = vapi.init_serverApi()
#
     is_started = False
#     # sa.startSimulation()
     print("step1")
     time.sleep(0.1)
     global port_number
     with grpc.insecure_channel(
             target='localhost:'+str(port_number),
             options=[('grpc.lb_policy_name', 'pick_first'),
                      ('grpc.enable_retries', 0), ('grpc.keepalive_timeout_ms',
                                                   10000)]) as channel:
      stub = simplus_pb2_grpc.SimPlusStub(channel)
#       # Timeout in seconds.
      try:
        response = stub.Start(simplus_pb2.WorldInfo(team_size=2,
                                                    robot_per_team=2,
                                                    color_sensor_size=2,
                                                    proximity_sensor_size=3,
                                                    check_points=
                                                    [simplus_pb2.CheckPoint(color='red', point=10),
                                                     simplus_pb2.CheckPoint(color='green', point=5)]), timeout=1)

        print("Client Received: " + response.name)
        my_team_id = 0
        r,game_duration=sa.set_name(response.name)
        print("game_duration=",game_duration)
        if r is None:
            r=0
        my_team_id = max(r, my_team_id)
        ra = vapi.init_robotApi()
        print("start precompute")
        ra.precompute()
        print("end precompute")
        print("Start")
        team_score = 0
        team_name = response.name
        i=0
        isExit=False
        while not is_started:
          print("Please click on the play button")
          is_started = sa.get_status(1)
        while not isExit:
            i=i+1
            #testtime=time.time_ns()
            is_started = sa.get_status(isOneshot=True)
            while not is_started:
                is_started = sa.get_status(isOneshot=True)
            
            if(is_started==2):
             #   ra.freezRobot();
                team_score+= (-5)
            a = time.process_time()

            image = ra.getCameraImage()
            thermal_image = ra.get_thermal_camera_image()
            image_array = np.array(image[0], dtype=np.uint8)
            thermal_image_array = np.array(thermal_image[0], dtype=np.uint8)
            colors = [ra.getColorSensor(i) for i in range(3)]

            proxim = [ra.getProximitySensor(i) for i in range(8)]

            pos = ra.getRobotPose()

            response = stub.Action(
                simplus_pb2.Observations(
                    server=simplus_pb2.ServerInfo(time=i, server_state='running', my_score=0, opp_score=1),
                    robots=[simplus_pb2.Observation(
                        camera=simplus_pb2.Image(w=image[1], h=image[2], raw=array.array('B', image_array).tobytes()),
                        colors=[simplus_pb2.Pixel(r=colors[i][0], g=colors[i][1], b=colors[i][2]) for i in range(3)],
                        distances=[simplus_pb2.Proximity(detected=proxim[i][0], distance=proxim[i][1]) for i in range(8)],
                        pos=simplus_pb2.Position(x=pos[0], y=pos[1], z=pos[2], roll=pos[3], pitch=pos[4], yaw=pos[5],
                                                 gps_enabled=ra.gps_enabled),
                        thermalCamera=simplus_pb2.Image(w=thermal_image[1], h=thermal_image[2], raw=array.array('B', thermal_image_array).tobytes())
                    ) for i in range(1)]
                )
            )

            for res in response.commands:
                #print('Robot ' + str(res.id) + ' Command: ' + str(res.linear) + ' ' + str(res.angular) + ' LED: ' + res.LED)
                ra.setRobotSpeed(linear=res.linear, angular=res.angular)
                ra.setLED(color=res.LED)
                robot_pose=ra.getRobotXYZ();
                for action in res.actions:
                    team_score += sa.findVictim(action.type,robot_pose[0],robot_pose[1],robot_pose[2])
                    action_score = sa.callAction(action.type,robot_pose[0],robot_pose[1],robot_pose[2],team_score)
                    if action=='exit' and action_score>0:
                     	isExit=True
                    team_score += action_score;
            
            team_score += ra.findCheckpoint()          
            team_score += ra.checkAllTraps()
            if team_score < 0:
            	team_score = 0
            sa.set_score(my_team_id, str(team_score))
            if isExit:
               sa.get_status(4)
            #print("dif time =",1000000000/(time.time_ns()-testtime))
            #testtime=time.time_ns()
        response = stub.End(
            simplus_pb2.Ending(server=simplus_pb2.ServerInfo(time=i, server_state='running', my_score=0, opp_score=1)))
        print('END IS: ' + response.message)
      except Exception as err:
          print("Waiting for Scratch")
          print("Client Received: " + "my_team_name")
          my_team_id = 0
          r=sa.set_name( "my_team_name")
          if r is None:
              r=0
          my_team_id = max(r, 0)
          ra = vapi.init_robotApi()
          st=simplus_scratch.ScratchThread(vapi,ra,sa)
          st.start()
          print("Start")
          team_score = 0
          team_name = "my_team_name"
          counter=0
          while True:

             while not is_started:
                  is_started = sa.get_status()
             time.sleep(0.25)
             counter += 1
             if (counter > 1000): break

if __name__ == '__main__':
    logging.basicConfig()
    run()
