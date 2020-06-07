from concurrent import futures
import logging
import grpc

import simplus_pb2
import simplus_pb2_grpc

# TODO: Import your own player file (a copy of sample.py which is filled with your code)
import sample
import player

# TODO: Set my_player to your own player
my_player = sample
# my_player = player

port_number = 4719


class Client(simplus_pb2_grpc.SimPlusServicer):
    def __init__(self, actor):
        self.actor = actor

    def Start(self, request, context):
        response = simplus_pb2.TeamInfo()
        try:
            self.actor.Start(request, response)
        except Exception as err:
            print(str(err))
        return response

    def Action(self, request, context):
        response = simplus_pb2.Commands()
        try:
            for id, observation in enumerate(request.robots):
                cmd = simplus_pb2.Command(id=id)
                self.actor.Play(id, request.server, observation, cmd)
                response.commands.append(cmd)
        except Exception as err:
            print(str(err))
        return response

    def End(self, request, context):
        response = simplus_pb2.Result()
        try:
            self.actor.End(request, response)
        except Exception as err:
            print(str(err))
        return response


def serve(actor):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simplus_pb2_grpc.add_SimPlusServicer_to_server(Client(actor), server)
    global port_number
    server.add_insecure_port('[::]:' + str(port_number))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve(my_player)
