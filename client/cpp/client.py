from concurrent import futures
import logging

import grpc

import simplus_pb2
import simplus_pb2_grpc
# cpp
import platform
import os
import ctypes as ct
import sys

try:
    file_extension = '.so'
    if platform.system() =='cli':
        file_extension = '.dll'
    elif platform.system() =='Windows':
        file_extension = '.dll'
    elif platform.system() == 'Darwin':
        file_extension = '.dylib'
    else:
        file_extension = '.so'
    libfullpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'player' + file_extension)
    player = ct.CDLL(libfullpath)
except:
    libfullpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'player.dll')
    player = ct.CDLL(libfullpath)



class Client(simplus_pb2_grpc.SimPlusServicer):

    def Start(self, request, context):
        response = simplus_pb2.TeamInfo()
        try:
         player.start.argtypes = [ct.c_int32,ct.c_int32,ct.c_int32,ct.c_int32]
         player.start.restype=ct.c_char_p;
         res=player.start(1,1,3,8)
         response.name = res.decode("utf-8") 
        except Exception as err:
            print(str(err))
        return response

    def Action(self, request, context):
      response = simplus_pb2.Commands()
      try:  
        for id, observation in enumerate(request.robots):
#             print(type(observation.camera.raw))
            cmd = simplus_pb2.Command(id=id)
            player.play.argtypes = [
            ct.POINTER(ct.c_int32),
            ct.POINTER(ct.c_int32),
            ct.POINTER(ct.c_int32),
            ct.POINTER(ct.c_int32),
            ct.POINTER(ct.c_float),
            ct.POINTER(ct.c_float),
            ct.POINTER(ct.c_int32),
            ct.POINTER(ct.c_float),
            ct.POINTER(ct.c_float),
            ct.POINTER(ct.c_float),
            ct.POINTER(ct.c_float),
            ct.POINTER(ct.c_float)
            ]
            player.play.restype=ct.c_char_p;
            c1 = (ct.c_int32*3)(observation.colors[0].r,observation.colors[0].g,observation.colors[0].b)
            c2 = (ct.c_int32*3)(observation.colors[1].r,observation.colors[1].g,observation.colors[1].b)
            c3 = (ct.c_int32*3)(observation.colors[2].r,observation.colors[2].g,observation.colors[2].b)
            detected = (ct.c_int32*8)(observation.distances[0].detected,observation.distances[1].detected,observation.distances[2].detected,observation.distances[3].detected,observation.distances[4].detected,observation.distances[5].detected,observation.distances[6].detected,observation.distances[7].detected)
            distances = (ct.c_float*8)(observation.distances[0].distance,observation.distances[1].distance,observation.distances[2].distance,observation.distances[3].distance,observation.distances[4].distance,observation.distances[5].distance,observation.distances[6].distance,observation.distances[7].distance)
            pos = (ct.c_float*3)(observation.pos.x,observation.pos.y,observation.pos.z)
            led=(ct.c_int32)()
            w_l=(ct.c_float)()
            w_a=(ct.c_float)()
            a_x=(ct.c_float)()
            a_y=(ct.c_float)()
            a_z=(ct.c_float)()
            a_name=ct.POINTER(ct.c_char)()
            res = player.play(c1,c2,c3,detected,distances,pos,ct.byref(led),ct.byref(w_l),ct.byref(w_a),ct.byref(a_x),ct.byref(a_y),ct.byref(a_z)) 
            cmd.linear = w_l.value
            cmd.angular = w_a.value
            if led.value==1:
              cmd.LED="red"
            elif  led.value==2:
              cmd.LED="green"
            elif  led.value==3:
              cmd.LED="blue"
            else:
              cmd.LED="akldjf"
            if(res.decode("utf-8")!=""):
              cmd.actions.append(simplus_pb2.Action(x=a_x.value,y=a_y.value,z=a_z.value,type=res.decode("utf-8")))
            response.commands.append(cmd)
      except Exception as err:
            print(str(err))
      return response

    def End(self, request, context):
      response = simplus_pb2.Result()
      try:  
        player.end.argtypes = []
        player.end.restype=ct.c_char_p;
        res=player_end()
        response.message = res.decode("utf-8") 
      except Exception as err:
            print(str(err))
      return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simplus_pb2_grpc.add_SimPlusServicer_to_server(Client(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
